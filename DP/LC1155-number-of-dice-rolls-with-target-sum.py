class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [[0 for _ in range(target+1)] for _ in range(n+1)]
        for d in range(1, min(k, target)+1):
            dp[1][d] = 1
            
        for i in range(2, n + 1):
            for dice in range(1, k+1):
                for score in range(1, target+1):
                    if score - dice > 0:
                        dp[i][score] += dp[i-1][score-dice]
                dp[i][score] %= 10 ** 9 + 7
        
        return dp[n][target]