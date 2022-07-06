class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k >= len(nums):
            return [max(nums)]
        ans = []
        window = []
        count = {}
        
        for i in range(k):
            heapq.heappush(window, -nums[i])
            count[nums[i]] = count.get(nums[i], 0) + 1
        ans.append(-window[0])
        
        for i in range(k, len(nums)):
            l, r = nums[i-k], nums[i]
            count[l] -= 1
            if count[l] == 0:
                del count[l]
            while window and -window[0] not in count:
                heapq.heappop(window)
            heapq.heappush(window, -r)
            count[r] = count.get(r, 0) + 1
            ans.append(-window[0])
        return ans