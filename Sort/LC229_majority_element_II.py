class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = []
        cnt = {}
        for num in nums:
            if num in cnt:
                cnt[num] += 1
            else:
                cnt[num] = 1
        
        threshold = floor(len(nums)/3.0)
        
        for key in cnt:
            if cnt[key] > threshold:
                ans.append(key)
                
        return ans