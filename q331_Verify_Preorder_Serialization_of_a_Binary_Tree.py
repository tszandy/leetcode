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
    def isValidSerialization(self, preorder: str) -> bool:
        count_null = 1
        for s in preorder.split(","):
            if count_null<=0:
                return False
            if s !="#":
                count_null+=1
            else:
                count_null-=1
        if count_null == 0:
            return True
        return False

sol = Solution()

# input
preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"

# output
output = sol.isValidSerialization(preorder)
# answer
answer = True
print(output, answer, answer == output)

# input
preorder = "1,#"

# output
output = sol.isValidSerialization(preorder)
# answer
answer = False
print(output, answer, answer == output)

# input
preorder = "9,#,#,1"

# output
output = sol.isValidSerialization(preorder)
# answer
answer = False
print(output, answer, answer == output)

# input
preorder = "#,7,6,9,#,#,#"

# output
output = sol.isValidSerialization(preorder)
# answer
answer = False
print(output, answer, answer == output)
