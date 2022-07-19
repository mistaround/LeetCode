class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_start, new_end = newInterval
        idx, n = 0, len(intervals)
        ans = []
        # add all intervals starting before newInterval
        while idx < n and intervals[idx][0] < new_start:
            ans.append(intervals[idx])
            idx += 1
        # add newInterval
        # if there is no overlap, just add the interval
        if not ans or ans[-1][-1] < new_start:
            ans.append(newInterval)
        # if there is an overlap, merge with the last interval
        else:
            ans[-1][1] = max(ans[-1][-1], new_end)
        
        # add next intervals, merge with newInterval if needed
        while idx < n:
            start, end = intervals[idx]
            if ans[-1][1] < start:
                ans.append(intervals[idx])
            else:
                ans[-1][1] = max(end, ans[-1][1])
            idx += 1
            
        return ans