class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        length = len(nums) - 1
        ans = [-1, -1]
        first = -1
        l = 0
        r = length
        m = floor((l + r)/2)
        
        # Find a match
        while l <= r:
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                first = m
                break
            m = floor((l + r)/2)
            
        if first == -1:
            return ans
        
        # Find left
        l = 0
        r = first
        m = floor((l + r)/2)
        while l <= r:
            print(m)
            if nums[m] != target:
                if m != length: 
                    if nums[m + 1] == target:
                        ans[0] = m + 1
                        break
                    else:
                        l = m + 1
                else:
                    ans[0] = first
                    break
            else:
                if m != 0:
                    if nums[m - 1] != target:
                        ans[0] = m
                        break
                    else:
                        r = m - 1
                else:
                    ans[0] = m
                    break
            m = floor((l + r)/2)
                    
        # Find Right
        l = first
        r = length
        m = floor((l + r)/2)
        while l <= r:
            if nums[m] != target:
                if m != 0:
                    if nums[m - 1] == target:
                        ans[1] = m - 1
                        break
                    else:
                        r = m - 1
                else:
                    ans[1] = first
                    break
            else:
                if m != length:
                    if nums[m + 1] != target:
                        ans[1] = m
                        break
                    else:
                        l = m + 1
                else:
                    ans[1] = m
                    break
            m = floor((l + r)/2)
            
        return ans
                    
            