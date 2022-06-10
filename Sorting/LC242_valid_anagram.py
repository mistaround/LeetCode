class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        cs = Counter(s)
        ct = Counter(t)
        cs.subtract(ct)
        print(cs.items())
        for key in dict(cs):
            if cs[key] != 0:
                return False
        return True