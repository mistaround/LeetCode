class Solution:
    def countAndSay(self, n: int) -> str:
        prev = ""
        ans = self.helper(n)
        return ans
    
    def helper(self, n):
        if n == 1:
            return "1"
        if n == 2:
            return "11"
        if n == 3:
            return "21"
        result = self.helper(n-1)
        current = ""
        prev = ""
        count = 0
        for s in result:
            if prev == "":
                prev = s
                count += 1
            else:
                if s == prev:
                    count += 1
                else:
                    current += str(count) + prev
                    prev = s
                    count = 1

        if current[-1] == prev:
            current = current[:-2] + str(count) + prev
        else:
            current += str(count) + prev
        return current
        