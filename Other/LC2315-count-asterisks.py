class Solution:
    def countAsterisks(self, s: str) -> int:
        count = 0
        flag = 0
        for i in range(len(s)):
            if s[i] == "|":
                flag += 1
            if flag % 2 != 0:
                continue
            if s[i] == "*":
                count += 1
        return count