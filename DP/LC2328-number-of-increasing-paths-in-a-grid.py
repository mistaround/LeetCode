class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        mod = 10 ** 9 + 7
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        def dfs(i, j):
            if dp[i][j] != 0:
                return dp[i][j]
            
            res = 1
            for dx, dy in dirs:
                x = i + dx
                y = j + dy
                if x >= 0 and y >= 0 and x < m and y < n and grid[x][y] > grid[i][j]:
                    res += dfs(x, y) % mod 
            
            dp[i][j] = res % mod
            return dp[i][j]
        
        count = 0
        for i in range(m):
            for j in range(n):
                count += dfs(i, j) % mod
        
        return count % mod