class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        returnList = []
        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            lp, rp = i+1, len(nums)-1
            target = -nums[i]
            # nums[lp] + nums[rp] should equal target
            while lp < rp:
                if nums[lp] + nums[rp] == target:
                    returnList.append([nums[i],nums[lp],nums[rp]])
                    lp += 1
                    rp -= 1
                    while lp < len(nums) and nums[lp] == nums[lp-1]:
                        lp += 1
                    while rp > lp and rp < len(nums)-1 and nums[rp] == nums[rp+1]:
                        rp -= 1
                elif nums[lp] + nums[rp] < target:
                    lp += 1
                else:
                    rp -= 1
                
                    
        return returnList