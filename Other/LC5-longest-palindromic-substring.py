class Solution:
    def longestPalindrome(self, s: str) -> str:
        maximum = -1
        ans = ""
        def spread(idx, s):
            c = 1
            l, r = idx, idx
            while True:
                if idx-c >= 0 and idx+c < len(s):
                    if s[idx-c] == s[idx+c]:
                        l, r = idx-c, idx+c
                        c += 1
                    else:
                        break
                else:
                    break
            return l, r
        
        for i in range(len(s)):
            l1, r1 = spread(i, s)
            tmp = s[:i] + "*" + s[i:]
            l2, r2 = spread(i, tmp)
            if r1 - l1 > maximum:
                maximum = r1 - l1
                ans = s[l1: r1+1]
            if r2 - l2 - 1 > maximum:
                maximum = r2 - l2 - 1
                ans = s[l2: r2]

        return ans
                
                
                