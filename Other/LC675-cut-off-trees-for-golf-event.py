class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        m, n = len(forest), len(forest[0])
        path = []
        for i in range(m):
            for j in range(n):
                if forest[i][j] > 1:
                    path.append((forest[i][j], (i,j))) 
        path.sort()

        def manhattan(s, t):
            return abs(s[0] - t[0]) + abs(s[1] - t[1])
        
        def A_star(s, t):
            queue = [((manhattan(s,t)), 0, s)]
            seen = set()
            
            while queue:
                h, d, cur = heapq.heappop(queue)
                if cur == t:
                    return d
                i, j = cur
                for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    x = i + dx
                    y = j + dy
                    if x < 0 or y < 0 or x == m or y == n \
                    or (x,y) in seen or forest[x][y] == 0:
                        continue
                    heapq.heappush(queue, (manhattan(t, (x,y))+d+1, d+1, (x,y)))
                    seen.add((x,y))
            
            return -1
        
        prev = (0, 0)
        ans = 0
        for height, coord in path:
            res = A_star(prev, coord)
            if res != -1:
                ans += res
                prev = coord
            else:
                return -1
            
        return ans