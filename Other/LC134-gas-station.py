class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # if i to j cannot make it, any k in [i,j], k to j will not make it too
        l = len(gas)
        C = sum(cost)
        G = sum(gas)
        if C > G:
            return -1
        S = 0
        idx = 0
        for i in range(l):
            S += gas[i] - cost[i]
            if S < 0:
                S = 0
                idx = i+1
        return idx