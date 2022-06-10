class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        orders = collections.defaultdict(list)

        for string in strs:
            sorted_ = ''.join(sorted(string))
            orders[sorted_].append(string)

        return orders.values()