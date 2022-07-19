class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for _ in range(n)] for _ in range(n)]
        ans = []
        # dia [-7,7] anti [0,14]
        def backtrack(row, cols, dias, antis):
            if row == n:
                tmp = []
                for i in range(n):
                    tmp.append("".join(board[i]))
                ans.append(tmp)
                return
            for col in range(n):
                if col not in cols and row-col not in dias and row+col not in antis:
                    cols.add(col)
                    dias.add(row - col)
                    antis.add(row + col)
                    board[row][col] = "Q"
                    backtrack(row + 1, cols, dias, antis)
                    cols.remove(col)
                    dias.remove(row - col)
                    antis.remove(row + col)
                    board[row][col] = "."
                        
        backtrack(0, set(), set(), set())
        return ans
        