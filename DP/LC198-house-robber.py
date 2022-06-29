class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0 for _ in range(n+1)]
        dp[1] = nums[0]
        max_prev = dp[0]
        for i in range(2,n+1):
            dp[i] = max_prev + nums[i-1]
            max_prev = max(dp[i-1], max_prev)
        return max(dp[-1], dp[-2])