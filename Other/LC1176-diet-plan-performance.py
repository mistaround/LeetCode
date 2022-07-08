class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        queue = []
        prev = 0
        ans = 0
        
        for i in calories:
            if len(queue) < k-1:
                queue.append(i)
                prev += i
                continue
            queue.append(i)
            prev += i
            
            if prev > upper:
                ans += 1
            elif prev < lower:
                ans -= 1
                
            prev -= queue.pop(0)
            

        return ans