class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        # dp[i] stands for how long we can go from dp[:i]
        dp = [0 for _ in range(length+1)]
        dp[1] = nums[0] + 1
        for i in range(1, length+1):
            if dp[i-1] >= i:
                dp[i] = max(dp[i-1], i + nums[i-1])
            if dp[i] >= length:
                return True
        return False