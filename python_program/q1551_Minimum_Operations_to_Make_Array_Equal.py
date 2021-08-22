from typing import List

class Solution:
    def minOperations(self, n: int) -> int:
        if n % 2 ==0:
            return (n//2)**2
        else:
            return ((n+1)//2)*(n//2)

    def minOperations_1(self, n: int) -> int:
        return ((n+1)//2)*(n//2)

sol = Solution()

print(sol.minOperations())