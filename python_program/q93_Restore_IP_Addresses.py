from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left,bisect_right
from itertools import count
import queue

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        if n>12:
            return []
        store_list = []
        return_list = []
        def backtracking(index):
            if (store_list and int(store_list[-1])>255) or len(store_list)>4:
                return
            if index == n:
                if len(store_list)==4:
                    return_list.append(".".join(store_list))
                return
            if store_list and not(store_list[-1]=="0"):
                store_list[-1]+=s[index]
                backtracking(index+1)
                store_list[-1] = store_list[-1][:-1]
                if len(store_list[-1])==0:
                    store_list.pop()
            store_list.append(s[index])
            backtracking(index+1)
            store_list.pop()
        backtracking(0)
        return return_list

sol = Solution()

# input
s = "25525511135"

# output
output = sol.restoreIpAddresses(s)
# answer
answer = ["255.255.111.35","255.255.11.135"]

print(output, answer, answer == output)

# input
s = "0000"

# output
output = sol.restoreIpAddresses(s)
# answer
answer = ["0.0.0.0"]

print(output, answer, answer == output)

# input
s = "1111"

# output
output = sol.restoreIpAddresses(s)
# answer
answer = ["1.1.1.1"]

print(output, answer, answer == output)

# input
s = "010010"

# output
output = sol.restoreIpAddresses(s)
# answer
answer = ["0.100.1.0","0.10.0.10"]

print(output, answer, answer == output)

# input
s = "101023"

# output
output = sol.restoreIpAddresses(s)
# answer
answer = ["101.0.2.3","10.10.2.3","10.1.0.23","1.0.102.3","1.0.10.23"]

print(output, answer, answer == output)

# input
s = "000"

# output
output = sol.restoreIpAddresses(s)
# answer
answer = []

print(output, answer, answer == output)
