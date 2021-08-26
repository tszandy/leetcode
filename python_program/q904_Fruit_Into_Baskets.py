from typing import List
from collections import Counter,defaultdict,deque
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left,bisect_right
from itertools import count,zip_longest
import queue

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        last_fruit = None
        last_fruit_start_index = -1
        basket_fruit_set = set()
        max_fruits = 0
        n = len(fruits)
        count_fruit = 0
        for i in range(n):
            fruit = fruits[i]
            if not(fruit in basket_fruit_set or len(basket_fruit_set)!=2):
                max_fruits = max(max_fruits,count_fruit)
                count_fruit = i-last_fruit_start_index
                for basket_fruit in list(basket_fruit_set):
                    if basket_fruit != last_fruit:
                        basket_fruit_set.remove(basket_fruit)
            basket_fruit_set.add(fruit)
            count_fruit +=1

            if last_fruit != fruit:
                last_fruit = fruit
                last_fruit_start_index = i
        max_fruits = max(max_fruits,count_fruit)

        return max_fruits


sol = Solution()

# input
fruits = [1,2,1]

# output
output = sol.totalFruit(fruits)
# answer
answer = 3

print(output, answer, answer == output)

# input
fruits = [0,1,2,2]

# output
output = sol.totalFruit(fruits)
# answer
answer = 3

print(output, answer, answer == output)

# input
fruits = [1,2,3,2,2]

# output
output = sol.totalFruit(fruits)
# answer
answer = 4

print(output, answer, answer == output)

# input
fruits = [3,3,3,1,2,1,1,2,3,3,4]

# output
output = sol.totalFruit(fruits)
# answer
answer = 5
print(output, answer, answer == output)

# input
fruits = [3,3,3,1,2,1,1,2,1,2,1,2,1,2,3,1,2,1,1,2,1,2,1,2,2,1,2,1,2,1,2,3,4]

# output
output = sol.totalFruit(fruits)
# answer
answer = 16
print(output, answer, answer == output)
