class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # To finally empty the stack
        heights.append(-1)
        stack = []
        area = 0
        for i in range(len(heights)):
            while len(stack) != 0 and heights[i] < heights[stack[-1]]:
                idx = stack.pop()
                left = -1 if len(stack) == 0 else stack[-1]
                area = max(heights[idx] * (i - left - 1), area)
            stack.append(i)
        return area