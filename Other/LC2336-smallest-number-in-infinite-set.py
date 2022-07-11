class SmallestInfiniteSet:

    def __init__(self):
        self.next = 1000
        self.set = set()
        self.heap = [i for i in range(1, 1001)]
        for i in self.heap:
            self.set.add(i)
        heapq.heapify(self.heap)
        
    def popSmallest(self) -> int:
        if self.heap:
            res = heapq.heappop(self.heap)
            self.set.remove(res)
            return res
        else:
            self.next += 1
            return self.next

    def addBack(self, num: int) -> None:
        if num not in self.set:
            self.set.add(num)
            heapq.heappush(self.heap, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)