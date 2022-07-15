class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 1:
            return nums
        
        f = False
        for s in range(n-1, 0, -1):
            if nums[s-1] < nums[s]:
                f = True
                break
        if not f:
            nums[:] = nums[::-1]
            return
        s = s - 1
        
        f = False
        for l in range(s+1, n):
            if nums[l] <= nums[s]:
                f = True
                break
        
        l = l - 1 if f else l

        nums[s], nums[l] = nums[l], nums[s]
        arr = nums[s+1:]
        nums[s+1:] = arr[::-1]
                
        