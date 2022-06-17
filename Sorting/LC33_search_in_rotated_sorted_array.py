class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        m = floor((l + r)/2)
        left = nums[l]
        right = nums[r]
        
        isRotated = False
        mInRotated = False
        tInRotated = False
        
        if left > right:
            isRotated = True
        
        if isRotated and target <= right:
            tInRotated = True
        
        while l <= r:
            if nums[m] == target:
                return m
            if isRotated:
                mInRotated = nums[m] < right
                if tInRotated:
                    if mInRotated:
                        if nums[m] > target:
                            r = m - 1
                        else:
                            l = m + 1
                    else:
                        l = m + 1 
                else:
                    if mInRotated:
                        r = m - 1
                    else:
                        if nums[m] > target:
                            r = m - 1
                        else:
                            l = m + 1
            else:
                if nums[m] > target:
                    r = m - 1
                else:
                    l = m + 1
            m = floor((l + r)/2)
        return -1