class Solution:
    dp = [[[0 for _ in range(7)] for _ in range(7)] for _ in range(10001)]
    
    def distinctSequences(self, n: int) -> int:
        
        def helper(n, p, pp):
            if n == 0:
                return 1
            if self.dp[n][p][pp] == 0:
                for d in range(1, 7):
                    if d != p and d != pp and (p == 0 or math.gcd(d, p) == 1):
                        self.dp[n][p][pp] = (self.dp[n][p][pp] + helper(n-1, d, p)) % ((10 ** 9) + 7)
            return self.dp[n][p][pp]
        
        return helper(n, 0, 0)