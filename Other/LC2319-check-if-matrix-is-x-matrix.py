class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    if i == j or i == n - j - 1:
                        return False
                else:
                    if i != j and i != n - j - 1:
                        return False
        return True
                