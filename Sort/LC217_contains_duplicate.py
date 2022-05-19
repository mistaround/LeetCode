class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numAppear = {}
        for i in nums:
            if i in numAppear:
                return True
            else:
                numAppear[i] = 1
        return False