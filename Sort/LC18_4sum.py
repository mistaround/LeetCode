class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        matches = []
        nums = sorted(nums)
        for p1 in range(len(nums)):
            if p1 > 0 and nums[p1] == nums[p1-1]:
                continue
            for p2 in range(p1+1, len(nums)):
                if p2 > p1 + 1 and nums[p2] == nums[p2-1]:
                    continue
                p3 = p2 + 1
                p4 = len(nums) - 1
                rest = target - nums[p1] - nums[p2]
                while p3 < p4:
                    if p3 > p2 + 1 and nums[p3] == nums[p3-1]:
                        p3 += 1
                        continue
                    if p4 < len(nums) - 1 and nums[p4] == nums[p4+1]:
                        p4 -= 1
                        continue
                    if nums[p3] + nums[p4] == rest:
                        matches.append([nums[p1],nums[p2],nums[p3],nums[p4]])
                        p3 += 1
                        p4 -= 1
                    elif nums[p3] + nums[p4] > rest:
                        p4 -= 1
                    else:
                        p3 += 1
        return matches
                