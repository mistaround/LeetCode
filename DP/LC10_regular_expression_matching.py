class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        # dp[i][j] stands for s[:i] matches p[:j]
        dp[0][0] = True
        # if i=0 which means s is empty, only if p = a*b*c*... can match
        for j in range(1, len(p) + 1):
            if p[j-1] == "*":
                dp[0][j] = dp[0][j-2]
        #
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j-1] == "." or p[j-1] == s[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # *
                    if p[j-1] == "*":
                        # skip or one or multiple
                        dp[i][j] = dp[i][j-2] or dp[i][j-1] or (dp[i-1][j] and (s[i-1] == p[j-2] or p[j-2] == "."))
                        
        return dp[-1][-1]