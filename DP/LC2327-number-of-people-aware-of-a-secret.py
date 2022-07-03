class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        dp = [1] * (n+1)
        new = [0] * (n+1)
        new[1] = 1
        
        for i in range(delay+1, n+1):
            if i > forget:
                for j in range(delay, forget+1):
                    new[i] += new[i-j]
                new[i] -= new[i-forget]
                dp[i] = dp[i-1] + new[i] - new[i-forget]
            else:
                for j in range(delay, i+1):
                    new[i] += new[i-j]
                dp[i] = dp[i-1] + new[i]
        
        return dp[n] % (10 ** 9 + 7)
        