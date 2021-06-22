from typing import List

class Solution:
    def mySqrt(self, x: int) -> int:
        
        l,r = 1,x
        while not (r-l == 1 and l**2<=x and r**2>x):
            m=(l+r)//2
            print(l,r)
            if m**2 == x:
                return m
            if m**2 <x:
                l=m
            if m**2>x:
                r=m
        return l
        

sol = Solution()

print(sol.mySqrt())