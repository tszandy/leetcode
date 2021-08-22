from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

class Solution:
#rolling hash
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        if n==0 and m ==0:
            return 0
        if m>n:
            return -1
        self.char_to_int_hash = lambda x:ord(x)-97

        needle_hash_value = self.hash_str(needle)
        string_hash_value = self.hash_str(haystack[:m])
        
        if string_hash_value == needle_hash_value:
            return 0

        mod_num = 26**(m-1)
        for i in range(m,n):
            string_hash_value%=mod_num
            string_hash_value=26*string_hash_value+self.char_to_int_hash(haystack[i])
            if string_hash_value == needle_hash_value:
                return i-m+1
        return -1
                
    def hash_str(self,string:str):
        if len(string) == 0:
            return 0
        return 26*self.hash_str(string[:-1])+self.char_to_int_hash(string[-1])

sol = Solution()


# input
haystack = "hello"
needle = "ll"
# output
output = sol.strStr(haystack, needle)
# answer
answer = 2
print(output, answer, answer == output)

# input
haystack = "aaaaa"
needle = "bba"
# output
output = sol.strStr(haystack, needle)
# answer
answer = -1
print(output, answer, answer == output)

# input
haystack = ""
needle = ""
# output
output = sol.strStr(haystack, needle)
# answer
answer = 0
print(output, answer, answer == output)

# input
haystack = ""
needle = "a"
# output
output = sol.strStr(haystack, needle)
# answer
answer = -1
print(output, answer, answer == output)
