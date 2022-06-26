class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        sign = (numerator > 0 and denominator > 0) or (numerator < 0 and denominator < 0)
        numerator = abs(numerator)
        denominator = abs(denominator)
        integer = numerator // denominator
        decimal = numerator % denominator
        
        if decimal == 0:
            return "-" + str(integer) if sign == False else str(integer)
        
        remainders = {}
        result = ""
        
        idx = 0
        flag = False
        print(integer,decimal)
        
        while True:
            print(decimal,result,remainders)
            if decimal in remainders:
                flag = True
                idx = remainders[decimal]
                break
            remainders[decimal] = idx
            if decimal * 10 < denominator:
                decimal *= 10
                result += "0"
            else:
                result += str(decimal * 10 // denominator)
                decimal = (decimal * 10) % denominator
                if decimal == 0:
                    break
            idx += 1
        
        ans = str(integer) + "."
        if flag == True:
            ans += result[0:idx] + "(" + result[idx:] + ")"
        else:
            ans += result
        if sign == False:
            ans = "-" + ans
        return ans