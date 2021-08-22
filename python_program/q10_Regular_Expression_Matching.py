from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache
import numpy as np
from heapq import *
from bisect import bisect_left

class Solution:
    @lru_cache(None)
    def isMatch(self, s: str, p: str) -> bool:
        if len(s)==0 and len(p)==0:
            return True
        elif len(s) == 0 and len(p)!=0 and p[-1]=="*":
            return self.isMatch(s,p[:-2])
        elif len(s) == 0 and len(p)!=0 and p[-1]!="*":
            return False
        elif len(s)!=0 and len(p)==0:
            return False

        last_s = s[-1]
        last_p = p[-1]
        star_p = None
        if last_p == "*":
            star_p = p[-2]
            if star_p ==".":
                return self.isMatch(s,p[:-2]) or self.isMatch(s[:-1],p[:-2]) or self.isMatch(s[:-1],p)
            elif star_p == last_s:
                return self.isMatch(s,p[:-2]) or self.isMatch(s[:-1],p[:-2]) or self.isMatch(s[:-1],p)
            else:
                return self.isMatch(s,p[:-2])

        else:
            if last_p ==".":
                return self.isMatch(s[:-1],p[:-1])
            elif last_s == last_p:
                return self.isMatch(s[:-1],p[:-1])
            else:
                return False

sol = Solution()


# input
s = "aa"

p = "a"

# output
output = sol.isMatch(s,p)
# answer
answer = False
print(output, answer, answer == output)

# input
s = "aa"

p = "a*"

# output
output = sol.isMatch(s,p)
# answer
answer = True
print(output, answer, answer == output)

# input
s = "ab"

p = ".*"

# output
output = sol.isMatch(s,p)
# answer
answer = True
print(output, answer, answer == output)

# input
s = "aab"

p = "c*a*b"

# output
output = sol.isMatch(s,p)
# answer
answer = True
print(output, answer, answer == output)

# input
s = "mississippi"

p = "mis*is*p*."

# output
output = sol.isMatch(s,p)
# answer
answer = False
print(output, answer, answer == output)

# input
s = "aasdfasdfasdfasdfas"

p = "aasdf.*asdf.*asdf.*asdf.*s"

# output
output = sol.isMatch(s,p)
# answer
answer = True
print(output, answer, answer == output)
