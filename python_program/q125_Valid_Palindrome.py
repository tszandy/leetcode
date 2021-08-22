from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left,bisect_right
from itertools import count

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join((filter(lambda x:97<=ord(x)<=122,s.lower())))
        n = len(s)
        for i in range(n//2):
            if s[n-1-i]!=s[i]:
                return False
        return True
    

sol = Solution()

# input
s = "A man, a plan, a canal: Panama"

# output
output = sol.isPalindrome(s)
# answer
answer = True
print(output, answer, answer == output)

# input
s = "race a car"

# output
output = sol.isPalindrome(s)
# answer
answer = False
print(output, answer, answer == output)

# input
s = " a"

# output
output = sol.isPalindrome(s)
# answer
answer = True
print(output, answer, answer == output)

# input
s = " "

# output
output = sol.isPalindrome(s)
# answer
answer = True
print(output, answer, answer == output)

# input
s = "0P"

# output
output = sol.isPalindrome(s)
# answer
answer = False
print(output, answer, answer == output)
