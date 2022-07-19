class Solution:
    ans = 1
    def longestConsecutive(self, nums: List[int]) -> int:
        parent = {}
        size = {}
        
        def find(x):
            p = parent.get(x, x)
            if p != x:
                parent[x] = find(p)
            return parent.get(x, x)
        
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                sx, sy = size.get(px, 1), size.get(py, 1)
                if sx < sy:
                    px, py = py, px
                parent[py] = px
                size[px] = sx + sy
            self.ans = max(size.get(px, 1), self.ans)
        if len(nums) == 0:
            return 0
        s = set(nums)
        for i in range(len(nums)):
            cur = nums[i]
            if cur - 1 in s:
                union(cur, cur-1)
            if cur + 1 in s:
                union(cur, cur+1)
        
        return self.ans