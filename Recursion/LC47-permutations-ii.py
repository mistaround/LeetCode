class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        counter = Counter(nums)
        path = []
        
        def backtrack():
            if len(path) == len(nums):
                ans.append(path[:])
            for key in counter:
                if counter[key] != 0:
                    counter[key] -= 1
                    path.append(key)
                    backtrack()
                    counter[key] += 1
                    path.pop()
        backtrack()
        
        return ans