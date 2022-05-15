class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        closet = 2454235220
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                current = nums[i] + nums[j] + nums[k]
                if abs(target - current) < abs(target - closet):
                    closet = current
                if current > target:
                    k -= 1
                elif current < target:
                    j += 1
                else:
                    return target
        return closet