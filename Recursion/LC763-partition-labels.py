class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans = []
        n = len(s)
        
        ls = {}
        rs = {}
        for c in s:
            rs[c] = rs.get(c, 0) + 1
        
        def check(ls, rs):
            if len(ls) == 0:
                return False
            for key in rs:
                if key in ls:
                    return False
            return True
        
        def split(left, ls, rs, prev):
            if len(rs) == 0:
                return
            next = -1
            for i in range(left, n + 1):
                if check(ls, rs):
                    next = i
                    ans.append(len(s[prev:i]))
                    break
                c = s[i]
                ls[c] = ls.get(c, 0) + 1
                rs[c] = rs.get(c, 0) - 1
                if rs[c] == 0:
                    del rs[c]
            if next != -1:
                split(next, {}, rs, next)
        
        split(0, ls, rs, 0)
            
        return ans
                