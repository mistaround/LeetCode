# Radix Sort
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        length = len(nums)
        if length <= 1:
            return 0
        # Using radix sort
        buckets = [[] for _ in range(10)]
        maximum = max(nums)
        digits = 0
        while maximum != 0:
            maximum = int(int(maximum)/10)
            digits += 1
        for i in range(1, digits+1):
            for num in nums:
                bit = int((num - num % (10 ** (i - 1))) / (10 ** (i - 1))) % 10 if i != 1 else num % 10
                buckets[bit].append(num)
            k = 0
            for j in range(10):
                while buckets[j]:
                    nums[k] = buckets[j].pop(0)
                    k += 1
        # Find maximum in sorted array
        maximum = 0
        for i in range(length - 1):
            difference = nums[i + 1] - nums[i]
            if difference > maximum:
                maximum = difference
        return maximum
        