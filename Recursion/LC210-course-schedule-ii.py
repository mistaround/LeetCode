class Solution:
    has_cycle = False
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for tar, pre in prerequisites:
            graph[tar].append(pre)
        
        ans = []
        on_path = [False for _ in range(numCourses)]
        finished = [False for _ in range(numCourses)]
        
        def dfs(idx):
            if on_path[idx]:
                self.has_cycle = True
                return False
            
            if finished[idx]:
                return True
            
            finished[idx] = True
            on_path[idx] = True
  
            res = True
            for course in graph[idx]:
                res = res and dfs(course)
            if res:
                ans.append(idx)
                
            on_path[idx] = False
            
            return True
        
        for i in range(numCourses):
            dfs(i)
        
        if self.has_cycle:
            return []
        else:
            return ans
            