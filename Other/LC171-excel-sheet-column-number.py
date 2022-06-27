class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        n = len(columnTitle) - 1
        base = ord('A') - 1
        ans = 0
        for c in columnTitle:
            ans += (ord(c) - base) * (26 ** n)
            n -= 1
        return ans
        
        