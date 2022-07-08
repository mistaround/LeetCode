class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ranks = {}
        sorted_list = sorted(arr)
        rank = 1
        for i in sorted_list:
            if i not in ranks:
                ranks[i] = rank
                rank += 1
        ans = []
        for i in arr:
            ans.append(ranks[i])
        return ans
            