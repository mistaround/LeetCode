class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        
        def helper(i, j, idx):
            if idx == len(word):
                return True
            if i == m or j == n or i < 0 or j < 0:
                return False
            if board[i][j] == word[idx]:
                tmp = board[i][j]
                board[i][j] = " "
                if helper(i+1, j, idx+1) or helper(i-1, j, idx+1) or helper(i, j+1, idx+1) or helper(i, j-1, idx+1):
                    return True
                board[i][j] = tmp
            return False
            
        
        for i in range(m):
            for j in range(n):
                if helper(i,j,0) == True:
                    return True
        
        return False
                    
                