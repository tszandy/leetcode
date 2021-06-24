from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        output_list = []
        l = 0
        r = n
        for i in s:
            if i == "I":
                output_list.append(l)
                l+=1
            else:
                output_list.append(n)
                n-=1
        output_list.append(l)
        return output_list

sol = Solution()


# input
s="IDID"
# output
output = sol.diStringMatch(s)
# answer
answer = [0,4,1,3,2]
print(output, answer, answer == output)

# input
s="III"
# output
output = sol.diStringMatch(s)
# answer
answer = [0,1,2,3]
print(output, answer, answer == output)

# input
s="DDI"
# output
output = sol.diStringMatch(s)
# answer
answer = [3,2,0,1]
print(output, answer, answer == output)
