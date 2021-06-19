from typing import List
import operator
import random



class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle)==1:
            return triangle[0][0]

        store = list(map(lambda x,y:min(x,y),triangle[-1][:-1],triangle[-1][1:]))
        for i in triangle[::-1][1:]:
            store = list(map(operator.add,store,i))
            if len(store)==1:
                return store[0]
            store = list(map(lambda x,y:min(x,y),store[:-1],store[1:]))
 

test_1 = [[random.randint(-10**4,10**4)for _ in range(i)]for i in range(1,200)]

sol = Solution()

print(sol.minimumTotal(test_1))
