class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0 for _ in range(n)] for _ in range(n)]
        num = 1
        for layer in range(n-1):
            for i in range(layer, n-layer-1):
                ans[layer][i] = num
                num += 1
            for i in range(layer, n-layer-1):
                ans[i][n-layer-1] = num
                num += 1
            for i in range(n-layer-1, layer, -1):
                ans[n-layer-1][i] = num
                num += 1
            for i in range(n-layer-1, layer, -1):
                ans[i][layer] = num
                num += 1
        if n % 2 != 0:
            ans[n//2][n//2] = num
        return ans