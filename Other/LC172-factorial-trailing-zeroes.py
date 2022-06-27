class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        n = n - (n % 5)
        for i in range(n, 0, -5):
            if i % 10000 == 0:
                ans += 4
            elif i % 3125 == 0:
                ans += 5
            elif i % 1000 == 0:
                ans += 3
            elif i % 625 == 0:
                ans += 4
            elif i % 125 == 0:
                ans += 3
            elif i % 100 == 0:
                ans += 2
            elif i % 25 == 0:
                ans += 2
            elif i % 10 == 0:
                ans += 1
            elif i % 5 == 0:
                ans += 1
        return ans if n < 5000 else ans + 1
                