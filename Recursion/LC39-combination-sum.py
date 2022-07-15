class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        lookup = set(candidates)
        n = len(candidates)
        
        def dfs(i, arr, res):
            cur = candidates[i]
            if cur == res:
                arr.append(cur)
                ans.append(arr)
                return
            elif cur > res:
                return
            else:
                for j in range(i, n):
                    tmp = arr[:]
                    tmp.append(cur)
                    dfs(j, tmp, res-cur)
                    
        for i in range(n):
            dfs(i, [], target)
        
        return ans
