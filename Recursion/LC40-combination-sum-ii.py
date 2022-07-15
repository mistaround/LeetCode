class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        ans = []
        candidates.sort()
        path = []
        
        def backtrack(idx, tar):
            if tar < 0 or idx == n:
                return
            
            if tar == 0:
                ans.append(path[:])
            
            for i in range(idx+1, n):
                if idx == i-1 or candidates[i] != candidates[i-1]:
                    path.append(candidates[i])
                    backtrack(i, tar - candidates[i])
                    path.pop(-1)
        
        for i in range(n):
            if i == 0 or candidates[i] != candidates[i-1]:
                path.append(candidates[i])
                backtrack(i, target-candidates[i])
                path = []
        
        return ans