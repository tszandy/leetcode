from typing import List

class Solution:
    def arrangeCoins(self, n: int) -> int:
        for i in range(1,math.ceil(sqrt(2*n+1/4)-1/2)+1):
            if n-i<0:
                return i-1
            n-=i
        return i

sol = Solution()

print(sol.arrangeCoins())