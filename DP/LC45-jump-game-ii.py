class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [sys.maxsize for i in range(n)]
        dp[0] = 0
        
        for i in range(1, n):
            for j in range(i, min(i+nums[i-1], n)):
                dp[j] = min(dp[j], dp[i-1] + 1)
        return dp[-1]
                