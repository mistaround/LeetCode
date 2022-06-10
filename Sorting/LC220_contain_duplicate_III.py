from sortedcontainers import SortedList
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        window = SortedList()
        for i in range(len(nums)):
            if i > k:
                window.remove(nums[i-k-1])
            # Gorgeous
            idx1 = window.bisect_left(nums[i] - t)
            idx2 = window.bisect_right(nums[i] + t)
            
            if idx1 != idx2:
                return True
            window.add(nums[i])
            
        return False