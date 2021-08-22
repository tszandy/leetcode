from typing import List

class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        if n == 1:
            return 1
        prime_or_not = [0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
        prime_count = sum(prime_or_not[:n])
        non_prime_count = n-prime_count
        
        p = 10**9+7
        
        p_fac = self.mod_factorial(prime_count,p)
        np_fac = self.mod_factorial(non_prime_count,p)
        
        return (p_fac*np_fac)%p
    
    def mod_factorial(self,n:int,p:int):
        if n ==1:
            return 1
        return n*self.mod_factorial(n-1,p) % p
        

sol = Solution()

print(sol.numPrimeArrangements())