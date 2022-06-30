class Solution:
    has_cycle = False
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for tar, pre in prerequisites:
            graph[tar].append(pre)
            
        finished = [False] * numCourses
        on_path = [False] * numCourses
        
        def dfs(idx, finished, on_path):
            if on_path[idx]:
                self.has_cycle = True
        
            if self.has_cycle or finished[idx]:
                return

            finished[idx] = True
            on_path[idx] = True
            for child in graph[idx]:
                dfs(child, finished, on_path)
            on_path[idx] = False
        
        for idx in range(numCourses):
            dfs(idx, finished, on_path)
        
        return not self.has_cycle