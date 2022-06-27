class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        sum1 = sum(nums1)
        sum2 = sum(nums2)
        diff1 = []
        diff2 = []
        for i in range(n):
            diff1.append(nums2[i] - nums1[i])
            diff2.append(nums1[i] - nums2[i])
        
        def kadane(diff):
            for i in range(1,n):
                if diff[i-1] > 0:
                    diff[i] += diff[i-1]
            return max(diff)
                
        return max(kadane(diff1) + sum1, kadane(diff2) + sum2)