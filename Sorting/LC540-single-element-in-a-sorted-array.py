class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # 1,1,2,2,3,4,4,8,8
        # 0,1,2,3,4,5,6,7,8
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l+r)//2
            if m != 0 and m != len(nums) - 1:
                if nums[m] == nums[m-1]:
                    if m % 2 == 1:
                        l = m + 1
                    else:
                        r = m - 1
                elif nums[m] == nums[m+1]:
                    if m % 2 == 0:
                        l = m + 1
                    else:
                        r = m - 1
                else:
                    return nums[m]
            else:
                return nums[m]
        return nums[l]