class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [- 1 12 123]
        # [234 34 4 -].reverse
    
        p1 = [1]
        p2 = [1]
        n = len(nums)
        for i in range(n-1):
            p1.append(nums[i] * p1[i])
            p2.append(nums[n-i-1] * p2[i])
        p2 = p2[::-1]
        ans = []
        for i in range(n):
            ans.append(p1[i] * p2[i])
        return ans