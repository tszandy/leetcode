from typing import List

class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        if a<b:
            return self.nthMagicalNumber(n,b,a)
        if a%b==0:
            return (n*b) %(10**9+7)
        lcm = int(a*b/gcd(a,b))
        count_in_lcm = int(lcm/a)+int(lcm/b)-1
        list_elem = set()
        for i in range(int(lcm/a)):
            list_elem.add(a*(i+1))
        for i in range(int(lcm/b)):
            list_elem.add(b*(i+1))
        list_elem = sorted(list(list_elem))
        return (lcm*((n-1)//count_in_lcm)+ list_elem[(n-1)%count_in_lcm])%(10**9+7)

sol = Solution()

print(sol.nthMagicalNumber())