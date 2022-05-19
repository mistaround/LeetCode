class Solution:
    def hIndex(self, citations: List[int]) -> int:
        lookup = {}
        citations = sorted(citations)
        for i in range(len(citations)):
            if citations[i] not in lookup:
                lookup[citations[i]] = len(citations[i:])
        h = 0
        for key in lookup:
            if lookup[key] >= h:
                if lookup[key] < key:
                    h = lookup[key]
                else:
                     h = key
        return h
