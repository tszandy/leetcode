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
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return None
        self.store_list = [root]
        self.connect_node()
        return root
        
    def connect_node(self):
        if self.store_list:
            bool_next_list = self.store_list[0].left!=None
            next_list = []
            n = len(self.store_list)
            for i in range(1,n):
                self.store_list[i-1].next = self.store_list[i]
                if bool_next_list:
                    next_list.append(self.store_list[i-1].left)
                    next_list.append(self.store_list[i-1].right)
            if bool_next_list:
                next_list.append(self.store_list[-1].left)
                next_list.append(self.store_list[-1].right)
                self.store_list = next_list
                self.connect_node()
        return

sol = Solution()

# input
[]
[1]
[1,2,3]
[1,2,3,4,5,6,7]
[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# output
output = sol.connect(root)
# answer
answer = ""
print(output, answer, answer == output)
