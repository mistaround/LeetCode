class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stack = []
        profit = 0
        for i in range(len(prices)):
            cur = prices[i]
            if len(stack) != 0 and cur > stack[-1]:
                profit = max(cur - stack[-1], profit)
            else:
                stack.append(cur)
        return profit