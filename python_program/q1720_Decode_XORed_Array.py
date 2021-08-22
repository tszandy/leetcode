from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        result = [first]
        next_int = first
        for i in encoded:
            next_int = next_int^i
            result.append(next_int)
            
        return result
        

sol = Solution()


# input
encoded = [1,2,3]
first = 1
# output
output = sol.decode(encoded,first)
# answer
answer = [1,0,2,1]
print(output, answer, answer == output)

# input
encoded = [6,2,7,3]
first = 4
# output
output = sol.decode(encoded,first)
# answer
answer = [4,2,0,7,4]
print(output, answer, answer == output)
