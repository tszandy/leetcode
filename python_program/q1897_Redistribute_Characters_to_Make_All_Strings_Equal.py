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
    def makeEqual(self, words: List[str]) -> bool:
        return all(map(lambda x:x%len(words)==0,reduce(lambda x,y:x+y,map(lambda x:Counter(x),words)).values()))

sol = Solution()

# input
words = ["abc","aabc","bc"]

# output
output = sol.makeEqual(words)
# answer
answer = True
print(output, answer, answer == output)

# input
words = ["ab","a"]

# output
output = sol.makeEqual(words)
# answer
answer = False
print(output, answer, answer == output)
