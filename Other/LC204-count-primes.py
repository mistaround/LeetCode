class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        isPrime = [True for _ in range(n)]
        isPrime[0] = isPrime[1] = False
        
        for p in range(2, ceil(math.sqrt(n))):
            if isPrime[p]:
                for num in range(p*p, n, p):
                    isPrime[num] = False
        
        return sum(isPrime)
        
            