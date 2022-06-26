class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        if len(nums) == 0:
            if lower == upper:
                return [str(lower)]
            else:
                return [str(lower) + "->" + str(upper)]
            
        ans = []
        prev = lower
        for i in range(len(nums)):
            if nums[i] == prev:
                prev += 1
            else:
                if nums[i] - prev == 1:
                    ans.append(str(prev))
                else:
                    ans.append(str(prev) + "->" + str(nums[i]-1))
                prev = nums[i] + 1
                
        if nums[-1] != upper:
            if nums[-1] + 1 == upper:
                ans.append(str(upper))
            else:
                ans.append(str(nums[-1]+1) + "->" + str(upper))
        return ans