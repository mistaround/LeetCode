class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # XOR
        ans = nums[0]
        for i in range(1,len(nums)):
            ans ^= nums[i]
        return ans