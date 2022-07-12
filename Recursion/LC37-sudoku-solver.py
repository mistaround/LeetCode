class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        goal = 0
        pos = []
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == ".":
                    goal += 1
                    pos.append((i,j))
        
        def check(x, y):
            res = []
            for num in range(1, 10):
                flag = True
                s = str(num) 
                for i in range(m):
                    if s == board[i][y]:
                        flag = False
                for i in range(n):
                    if s == board[x][i]:
                        flag = False
                r, c = x // 3, y // 3
                for dx in range(3):
                    for dy in range(3):
                        if s == board[r*3+dx][c*3+dy]:
                            flag = False
                if flag == True:
                    res.append(s)
            return res
        
        def fill(count):
            if count == goal:
                return True
            x, y = pos[count]
            candidates = check(x,y)
            while candidates:
                num = candidates.pop()
                board[x][y] = num
                if fill(count+1):
                    return True
            else:
                board[x][y] = "."
                return False
            return True
        
        fill(0)
        return board
        
        
                    