class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        s = 0
        prefix = {0:1}
        for i in range(len(nums)):
            s += nums[i]
            if s - k in prefix:
                ans += prefix[s - k]
            prefix[s] = prefix.get(s, 0) + 1
        return ans