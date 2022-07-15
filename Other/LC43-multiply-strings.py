class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        
        n1 = len(num1)
        n2 = len(num2)
        ans = 0
        
        o1 = 0
        for i in range(n2-1,-1,-1):
            o2 = 0
            for j in range(n1-1,-1,-1):
                ans += int(num1[j]) * int(num2[i]) * (10 ** o1) * (10 ** o2)
                o2 += 1
            o1 += 1
        
        return str(ans)
            