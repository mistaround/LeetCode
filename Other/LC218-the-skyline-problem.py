class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        ans = []
        sorted_buildings = []
        queue = [0]
        heapq.heapify(queue)
        
        for arr in buildings:
            sorted_buildings.append([arr[0], -arr[2]])
            sorted_buildings.append([arr[1], arr[2]])
        sorted_buildings.sort()
        
        for x, h in sorted_buildings:
            prev = queue[0]
            if h <= 0:
                heapq.heappush(queue, h)
            else:
                queue.remove(-h)
                heapq.heapify(queue)
            
            if prev != queue[0]:
                ans.append([x, -queue[0]])
        
        return ans
        