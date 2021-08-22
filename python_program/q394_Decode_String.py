from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache
import numpy as np
from heapq import *
from bisect import bisect_left

class Solution:
    def decodeString(self, s: str) -> str:
        store_list = []
        
        store_num = ""
        store_str = ""
        return_str = ""
        for c in s[::-1]:
            if 48<=ord(c)<=57:
                store_num = c + store_num
            else:
                if store_num and store_str:
                    if store_list:
                        store_list[-1] = int(store_num)*store_str + store_list[-1]
                    else:
                        return_str = int(store_num)*store_str + return_str
                    store_num = ""
                    store_str = ""
                if c =="]":
                    store_list.append("")
                elif c =="[":
                    store_str +=store_list.pop()
                else:
                    if store_list:
                        store_list[-1] = c + store_list[-1]
                    else:
                        return_str = c + return_str
        if store_num and store_str:
            if store_list:
                store_list[-1] = int(store_num)*store_str + store_list[-1]
            else:
                return_str = int(store_num)*store_str + return_str
            store_num = ""
            store_str = ""
        return return_str

sol = Solution()


# input
s = "3[a]2[bc]"

# output
output = sol.decodeString(s)
# answer
answer = "aaabcbc"
print(output, answer, answer == output)

# input
s = "3[a2[c]]"

# output
output = sol.decodeString(s)
# answer
answer = "accaccacc"
print(output, answer, answer == output)

# input
s = "2[abc]3[cd]ef"

# output
output = sol.decodeString(s)
# answer
answer = "abcabccdcdcdef"
print(output, answer, answer == output)

# input
s = "abc3[cd]xyz"

# output
output = sol.decodeString(s)
# answer
answer = "abccdcdcdxyz"
print(output, answer, answer == output)
