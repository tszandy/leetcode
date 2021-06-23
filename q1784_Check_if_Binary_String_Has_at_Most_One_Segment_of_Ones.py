from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return len(list(filter(lambda x:x!="",s.split("0"))))==1

sol = Solution()


# input
s = "1001"
# output
output = sol.checkOnesSegment(s)
# answer
answer = False
print(output, answer, answer == output)

# input
s = "110"
# output
output = sol.checkOnesSegment(s)
# answer
answer = True
print(output, answer, answer == output)
