class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        def dfs(i,j):
            if i == -1 or i == m or j == -1 or j == n:
                return
            if grid[i][j] != "1":
                return
            grid[i][j] = "*"
            
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i,j)
                    ans += 1 
                    
        return ans