class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        store = [False for _ in range(n)]
        stack = []
        
        for i in range(n):
            if s[i] == ")":
                if stack:
                    idx = stack.pop(-1)
                    store[idx], store[i] = True, True
            else:
                stack.append(i)
        ans = 0
        count = 0
        for i in range(n):
            if store[i] == False:
                count = 0
            else:
                count += 1
                ans = max(count, ans)
        
        return ans
                    
                