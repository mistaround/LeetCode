class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = []
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotten.append((i,j))
        ans = -1
        while len(rotten) != 0:
            next = []
            while len(rotten) != 0:
                i, j = rotten.pop(0)
                for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    x = i + dx
                    y = j + dy
                    if x >= 0 and y >= 0 and x < m and y < n and grid[x][y] == 1:
                        grid[x][y] = 2
                        next.append((x,y))
            ans += 1
            rotten = next
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
                
        if ans == -1:
            return 0
        
        return ans