class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        parent = {}
        count = 0
        ocean = [[0 for _ in range(n)] for _ in range(m)]
        ans = []
        
        def find(x):
            p = parent.get(x, x)
            if x != p:
                parent[x] = find(p)
            return parent.get(x, x)
        
        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False
            parent[py] = px
            return True
        
        for i, j in positions:
            if ocean[i][j] != 1:
                neighbour = 1
                ocean[i][j] = 1

                for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                    x, y = i+dx, j+dy
                    if x < 0 or y < 0 or x >= m or y >= n or ocean[x][y] == 0:
                        continue
                    if union((i,j),(x,y)):
                        neighbour -= 1

                count += neighbour
            ans.append(count)
        
        return ans