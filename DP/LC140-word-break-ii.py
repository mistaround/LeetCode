class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        lookup = set(wordDict)
        n = len(s)
        st = [0]
        words = [[] for _ in range(n+1)]
        for i in range(1,n+1):
            flag = False
            for last in st:
                cur = s[last:i]
                if cur in lookup:
                    if flag == False:
                        st.append(i)
                        flag = True
                    words[i].append(cur)
        ans = []
        
        def dfs(l, prev):
            if l == 0:
                ans.append(prev.strip())
                return
            for w in words[l]:
                dfs(l-len(w), w + " " + prev)
        dfs(n, "")
            
        return ans