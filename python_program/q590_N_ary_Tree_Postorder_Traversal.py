from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left,bisect_right
from itertools import count

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        self.return_list = []
        
    def post_order(self,node):
        if node == None:
            return
        for c in node.children:
            self.post_order(c)
        self.return_list.append(node.val)


sol = Solution()

# input
root = [1,null,3,2,4,null,5,6]

# output
output = sol.postorder(root)
# answer
answer = ""
print(output, answer, answer == output)

# input
root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]

# output
output = sol.postorder(root)
# answer
answer = ""
print(output, answer, answer == output)
