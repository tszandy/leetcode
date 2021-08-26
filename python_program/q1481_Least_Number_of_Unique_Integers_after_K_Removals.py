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
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = Counter(arr)
        sorted_counter = sorted(counter.items(),key = lambda x:x[1])
        while sorted_counter:
            key,val = sorted_counter.pop(0)
            if k-val<0:
                return len(sorted_counter)+1
            k-=val
        return 0 

sol = Solution()

# input
[5,5,4]
0
[5,5,4]
1
[5,5,4]
2
[5,5,4]
3
[4,3,1,1,3,3,2]
3

# output
output = sol.func()
# answer
answer = ""
print(output, answer, answer == output)
