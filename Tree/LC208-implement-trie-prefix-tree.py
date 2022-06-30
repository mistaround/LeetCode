class Node:
    
    def __init__(self):
        self.children = {}

class Trie:

    def __init__(self):
        self.root = Node()
        self.storage = set()

    def insert(self, word: str) -> None:
        node = self.root
        self.storage.add(word)
        for c in word:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
                
    def search(self, word: str) -> bool:
        if word in self.storage:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c] 
        return True
        
    

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)