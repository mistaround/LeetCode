class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        lookup = set(wordDict)
        n = len(s)
        st = [0]
        for i in range(1,n+1):
            for last in st:
                cur = s[last:i]
                if cur in lookup:
                    if i == n:
                        return True
                    st.append(i)
                    break
        return False
                