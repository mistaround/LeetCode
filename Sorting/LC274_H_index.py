class Solution:
    def hIndex(self, citations: List[int]) -> int:
        try:
            while True:
                citations.remove(0)
        except:
            pass
        if len(citations) == 0:
            return 0
        citations = sorted(citations)
        length = len(citations)
        for i in range(length):
            if length - i <= citations[i]:
                break
        return length - i
        