class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        length = len(height)
        maxLeft = [0 for i in range(length)]
        maxRight = [0 for i in range(length)]
        
        maxLeft[0] = height[0]
        for i in range(1,length):
            maxLeft[i] = max(maxLeft[i-1], height[i])
            
        maxRight[length-1] = height[length-1]
        for i in range(length-2, -1, -1):
            maxRight[i] = max(maxRight[i+1], height[i])
            
        for i in range(length):
            ans += min(maxLeft[i], maxRight[i]) - height[i]
            
        return ans
        

        