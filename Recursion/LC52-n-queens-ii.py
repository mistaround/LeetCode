class Solution:
    ans = 0
    def totalNQueens(self, n: int) -> int:
        def backtrack(row, cols, dias, antis):
            if row == n:
                self.ans += 1
                return
            for col in range(n):
                if col not in cols and row-col not in dias and row+col not in antis:
                    cols.add(col)
                    dias.add(row-col)
                    antis.add(row+col)
                    backtrack(row+1, cols, dias, antis)
                    cols.remove(col)
                    dias.remove(row-col)
                    antis.remove(row+col)
        backtrack(0, set(), set(), set())
        return self.ans
        
                    