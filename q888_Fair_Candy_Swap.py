from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        alice_sum = sum(aliceSizes)
        bob_sum = sum(bobSizes)
        difference = (bob_sum - alice_sum)//2
        alice_candy_set = set(aliceSizes)
        bob_candy_set = set(bobSizes)
        for alice_candy in alice_candy_set:
            if alice_candy+difference in bob_candy_set:
                return [alice_candy,alice_candy+difference]

sol = Solution()


# input
aliceSizes = [1,1]
bobSizes = [2,2]
# output
output = sol.fairCandySwap(aliceSizes,bobSizes)
# answer
answer = [1,2]
print(output, answer, answer == output)

# input
aliceSizes = [1,2]
bobSizes = [2,3]
# output
output = sol.fairCandySwap(aliceSizes,bobSizes)
# answer
answer = [1,2]
print(output, answer, answer == output)

# input
aliceSizes = [2]
bobSizes = [1,3]
# output
output = sol.fairCandySwap(aliceSizes,bobSizes)
# answer
answer = [2,3]
print(output, answer, answer == output)

# input
aliceSizes = [1,2,5]
bobSizes = [2,4]
# output
output = sol.fairCandySwap(aliceSizes,bobSizes)
# answer
answer = [5,4]
print(output, answer, answer == output)
