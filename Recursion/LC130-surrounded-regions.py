class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Make O that in the border marked and not change, change all O not marked
        m = len(board)
        n = len(board[0])
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        
        def dfs(x,y):
            board[x][y] = "#"
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx >= 0 and ny >= 0 and nx < m and ny < n:
                    if board[nx][ny] == "O":
                        dfs(nx, ny)
        
        for i in range(m):
            if board[i][0] == "O":
                dfs(i,0)
            if board[i][n-1] == "O":
                dfs(i,n-1)
        for j in range(n):
            if board[0][j] == "O":
                dfs(0,j)
            if board[m-1][j] == "O":
                dfs(m-1,j)
        for i in range(m):
            for j in range(n):
                if board[i][j] == "#":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
        