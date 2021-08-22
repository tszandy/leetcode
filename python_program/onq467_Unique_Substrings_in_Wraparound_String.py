from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left
from itertools import count

class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        
        n = len(p)
        
        cur_ord = ord(p[0])
        store_list = [1]
        for i in range(1,n):
            if ord(p[i]) == cur_ord+1 or (ord(p[i]) == 97 and cur_ord==122):
                store_list[-1]+=1
                cur_ord = ord(p[i])
            else:
                cur_ord = ord(p[i])
                store_list.append(1)
        print(store_list)
        map_func = lambda x:x*(x+1)//2
        return sum(map(map_func,store_list))

sol = Solution()

# input

# output
output = sol.func()
# answer
answer = ""
print(output, answer, answer == output)
