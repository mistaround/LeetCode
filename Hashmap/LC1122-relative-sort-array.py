class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counter = Counter(arr1)
        ans = []
        for i in range(len(arr2)):
            for j in range(counter[arr2[i]]):
                ans.append(arr2[i])
        for i in arr2:
            del counter[i]
        tmp = []
        for key in counter:
            for i in range(counter[key]):
                tmp.append(key)
        tmp = sorted(tmp)
        ans += tmp
        return ans
        
        