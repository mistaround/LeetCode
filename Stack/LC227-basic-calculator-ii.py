class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        nums = re.split("\+|\-|\*|\/", s)
        operators = list(filter(lambda x: x != '', re.split("\d+", s)))
        n = len(operators)
        stack = [int(nums[0])]
        
        for i in range(n):
            cur = operators[i]
            num = int(nums[i+1])
            if cur == "+":
                stack.append(num)
            elif cur == "-":
                stack.append(-num)
            elif cur == "*":
                prev = stack.pop(-1)
                stack.append(prev * num)
            else:
                prev = stack.pop(-1)
                stack.append(int(prev / num))
        
        return int(sum(stack))
            
                