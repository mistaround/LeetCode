class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        if n < 0:
            return 1/self.helper(x,-n)
        else:
            return self.helper(x,n)
    
    def helper(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x
        
        if n % 2 == 0:
            res = self.helper(x, n/2)
            return res * res
        else:
            res = self.helper(x, (n-1)/2)
            return x * res * res
        