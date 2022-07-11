class FreqStack:

    def __init__(self):
        self.count = Counter()
        self.heap = []
        self.index = 0

    def push(self, val: int) -> None:
        self.count[val] += 1
        self.index += 1
        heapq.heappush(self.heap, (-self.count[val], -self.index, val))

    def pop(self) -> int:
        _, _, val = heapq.heappop(self.heap)
        self.count[val] -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()