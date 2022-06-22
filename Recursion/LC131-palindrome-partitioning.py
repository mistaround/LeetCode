class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]

        for j in range(n):
            for i in range(j+1):
                if i == j:
                    dp[i][j] = True
                else:
                    dp[i][j] = (s[i] == s[j]) and (i+1 > j-1 or dp[i+1][j-1])
        path = []
        
        def dfs(s, idx):
            if idx == n:
                ans.append([*path])
                return
            for i in range(n):
                if dp[idx][i] == False:
                    continue
                path.append(s[idx:i+1])
                dfs(s, i+1)
                path.pop()
            
        dfs(s, 0)
        return ans