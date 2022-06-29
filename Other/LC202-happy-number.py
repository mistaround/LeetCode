class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        cur = n
        
        while cur not in seen:
            seen.add(cur)
            tmp = 0
            for c in str(cur):
                tmp += int(c) * int(c)
            cur = tmp
            if cur == 1:
                return True
            
        return False