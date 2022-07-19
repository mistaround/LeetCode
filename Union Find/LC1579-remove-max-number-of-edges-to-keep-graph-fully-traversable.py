class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        
        def find(x):
            p = parent.get(x, x)
            if p != x:
                parent[x] = find(p)
            return parent.get(x, x)
        
        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False
            parent[py] = px
            return True
        
        ans = 0
        graph = defaultdict(list)
        parent = {}
        count = 0
        
        for t, u, v in edges:
            graph[t].append((u, v))
            
        for u, v in graph[3]:
            if not union(u, v):
                ans += 1
            else:
                count += 1
                
        tmp = parent.copy()
        prev = count
        for u, v in graph[1]:
            if not union(u, v):
                ans += 1
            else:
                prev += 1
        if prev != n-1:
            return -1
            
        parent = tmp
        prev = count
        for u, v in graph[2]:
            if not union(u, v):
                ans += 1
            else:
                prev += 1
        if prev != n-1:
            return -1
            
        return ans
        