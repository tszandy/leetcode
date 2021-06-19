from typing import List

class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        list_store = [a,b,c]
        list_store = sorted(list_store)
        if list_store[2]>=sum(list_store[:2]):
            return sum(list_store[:2])
        else:
            return sum(list_store)//2

sol = Solution()

print(sol.maximumScore())