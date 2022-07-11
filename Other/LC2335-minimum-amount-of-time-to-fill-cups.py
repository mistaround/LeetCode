class Solution:
    def fillCups(self, amount: List[int]) -> int:
        ans = 0
        while True:
            amount.sort()
            if amount[2] == 0:
                break
            if amount[0] != 0:
                amount[0] -= 1
            elif amount[1] != 0:
                amount[1] -= 1
            amount[2] -= 1
            ans += 1
        return ans
            
        