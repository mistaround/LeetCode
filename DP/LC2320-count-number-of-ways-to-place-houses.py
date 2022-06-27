class Solution:
    def countHousePlacements(self, n: int) -> int:
        dp = [[0,0] for _ in range(n+1)]
        ans = 0
        dp[0][0] = 1
        for i in range(1,n+1):
            dp[i][0] = dp[i-1][0] + dp[i-1][1]
            dp[i][1] = dp[i-1][0]
        ans = dp[n][0] + dp[n][1]
        ans *= ans
        return ans % (10**9 + 7)
            