from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        strings = []
        for i in range(len(nums)):
            string = str(nums[i])
            strings.append(string)
        strings = sorted(strings, reverse=True)
        def comparator(a, b):
            length = max(len(a),len(b))
            a_ = int(a + b[:length - len(a)])
            b_ = int(b + a[:length - len(b)])
            if a_ == b_:
                if int(a + b) > int (b + a):
                    return 1
                else:
                    return -1
            return a_ - b_ 
        strings = sorted(strings, key=cmp_to_key(comparator), reverse=True)
        result = ""
        for string in strings:
            result += string
        if int(result) == 0:
            return "0"
        return result