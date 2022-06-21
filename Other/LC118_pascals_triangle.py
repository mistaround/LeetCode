class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for n in range(1,numRows+1):
            row = []
            last = []
            if n > 1:
                last = ans[n-2]
            for i in range(n):
                if i == 0 or i == n-1:
                    row.append(1)
                else:
                    row.append(last[i-1] + last[i])
            ans.append(row)
        return ans
            