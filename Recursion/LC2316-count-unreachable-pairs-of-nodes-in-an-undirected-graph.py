class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
            
        seen = set()
        
        def dfs(node):
            if node in seen:
                return 0
            seen.add(node)
            res = 1
            for i in graph[node]:
                res += dfs(i)
            return res
        
        total = 0
        groups = []
        for i in range(n):
            res = dfs(i)
            total += res
            groups.append(res)
        ans = 0
        for i in groups:
            ans += i * (total - i)
        return ans // 2