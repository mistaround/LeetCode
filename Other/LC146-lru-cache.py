class Node:
    
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.lru_node = Node()
        self.mru_node = Node()
        self.mru_node.next = self.lru_node
        self.lru_node.prev = self.mru_node
    
    def delete(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
        
    def insert(self, node):
        next = self.mru_node.next
        self.mru_node.next = node
        node.prev = self.mru_node
        node.next = next
        next.prev = node
        
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            val = node.val
            self.delete(node)
            self.insert(node)
            return val
        return -1
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.delete(node)
            node = Node(key, value)
            self.insert(node)
            self.cache[key] = node
        else:
            node = Node(key, value)
            if len(self.cache) < self.capacity:
                self.insert(node)
            else:
                self.cache.pop(self.lru_node.prev.key)
                self.delete(self.lru_node.prev)
                self.insert(node)
            self.cache[key] = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)