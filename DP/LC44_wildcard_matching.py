class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        # dp row stand for char in s, col stand for char in p
        # dp[i][j] meaning: 0:ith in s matches 0:jth in p
        dp = [[False for _ in range(m+1)] for _ in range(n+1)]
        dp[0][0] = True
        # If p is empty, no unempty s should be matched, so dp[0][j] = false
        # If s is empty, only if p = ****... can match
        for i in range(1,n+1):
            if p[i-1] == "*" and dp[i-1][0]:
                dp[i][0] = True
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                if p[j-1] == "*":
                    dp[j][i] = dp[j-1][i-1] or dp[j][i-1] or dp[j-1][i]
                elif p[j-1] == "?":
                    dp[j][i] = dp[j-1][i-1]
                else:
                    if p[j-1] == s[i-1]:
                        dp[j][i] = dp[j-1][i-1]
                    else:
                        dp[j][i] = False
            
        return dp[-1][-1]
                    