class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n < 3:
            return list(range(n))
        graph = defaultdict(set)
        for x, y in edges:
            graph[x].add(y)
            graph[y].add(x)
        
        queue = deque([i for i in range(n) if len(graph[i]) == 1])
        unseen = n
        
        while True:
            l = len(queue)
            
            if l == unseen:
                return list(queue)
            
            for _ in range(l):
                cur = queue.pop()
                parent = graph[cur].pop()
                graph[parent].remove(cur)
                unseen -= 1
                if len(graph[parent]) == 1:
                    queue.appendleft(parent)

            
        