from typing import List

class Solution:
    def countOrders(self, n: int) -> int:
        if n ==1:return 1
        p = 10**9+7
        mod_fac = self.mod_factorial(2*n,p)
        mod_pow = self.mod_power(2,n,p)
        if mod_fac % mod_pow ==0:
            return int(mod_fac/mod_pow) 
        else:
            mod_pow_inverse = self.mod_inverse(mod_pow,p)
            return int(mod_fac *mod_pow_inverse%p)
        
        
    def mod_power(self,n:int,po:int,p:int):
        if po == 1:
            return n
        if po%2==0:
            return self.mod_power(n**2,po//2,p)%p
        else:
            return (n*self.mod_power(n**2,po//2,p))%p

    def mod_factorial(self,n:int,p:int):
        if n <=1:
            return 1
        return (n*self.mod_factorial(n-1,p)) % p
    
    def mod_inverse(self,a:int, m:int):
        m0 = m
        y = 0
        x = 1

        if (m == 1):
            return 0

        while (a > 1):

            q = a // m

            t = m
            m = a % m
            a = t
            t = y
            y = x - q * y
            x = t
        if (x < 0):
            x = x + m0

        return x


sol = Solution()

print(sol.countOrders())