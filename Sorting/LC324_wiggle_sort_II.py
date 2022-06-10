class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        nums.sort()
        ans = [0 for _ in range(length)]
        idx = length - 1
        for i in range(1,length,2):
            ans[i] = nums[idx]
            idx -= 1
        for i in range(0,length,2):
            ans[i] = nums[idx]
            idx -= 1
        nums[:] = ans[:]