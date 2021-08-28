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
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        hq = []
        result = []
        counter = Counter(barcodes)
        for key,val in counter.items():
            heappush(hq,(-val,key))
        
        while hq:
            val_1,key_1 = heappop(hq)
            val_2,key_2 = heappop(hq)
            result.append(key_1)
            result.append(key_2)
            if val_1+1!=0:
                heappush(hq,(val_1+1,key_1))
            if val_2+1!=0:
                heappush(hq,(val_2+1,key_2))
        return result

sol = Solution()

# input
barcodes = [1,2,3]

# output
output = sol.rearrangeBarcodes(barcodes)
# answer
answer = ""
print(output, answer, answer == output)

# input
barcodes = [1,1,1,2,2,2]

# output
output = sol.rearrangeBarcodes(barcodes)
# answer
answer = ""
print(output, answer, answer == output)

# input
barcodes = [1,1,1,1,2,2,3,3]

# output
output = sol.rearrangeBarcodes(barcodes)
# answer
answer = ""
print(output, answer, answer == output)

# input
barcodes = [1,1,2,2,3,3,4,4,5,5]

# output
output = sol.rearrangeBarcodes(barcodes)
# answer
answer = ""
print(output, answer, answer == output)

# input
barcodes = [1,1,2,2,3,3,4,4,5,6,6,6]

# output
output = sol.rearrangeBarcodes(barcodes)
# answer
answer = ""
print(output, answer, answer == output)
