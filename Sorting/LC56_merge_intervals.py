class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        returnList = []
        intervals = sorted(intervals, key=lambda intervals: intervals[0])
        print(intervals)
        cache = intervals[0]
        for i in range(1,len(intervals)):
            if (intervals[i][0] <= cache[1]):
                cache = [cache[0], max(cache[1], intervals[i][1])]
            else:
                returnList.append(cache)
                cache = intervals[i]
        returnList.append(cache)
        return returnList