import heapq as hq
class MedianFinder:
    # Two Heap
    def __init__(self):
        self.maxHeap = []
        self.minHeap = []
        self.count = 0

    def addNum(self, num: int) -> None:
        self.count += 1
        minTop = -hq.heappushpop(self.minHeap, num)
        if self.count %2 != 0:
            hq.heappush(self.maxHeap, minTop)
        else:
            maxTop = -hq.heappushpop(self.maxHeap, minTop)
            hq.heappush(self.minHeap, maxTop)

    def findMedian(self) -> float:
        if self.count %2 != 0:
            return -self.maxHeap[0]
        else:
            return (-self.maxHeap[0] + self.minHeap[0]) / 2