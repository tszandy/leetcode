from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left,bisect_right
from itertools import count
import queue

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
        self.store_list = []
        self.pre_order_traversal(root,0)
        for level_list in self.store_list:
            for i in range(len(level_list)-1):
                level_list[i].next = level_list[i+1]
        return root
        
    
    def pre_order_traversal(self,node,level):
        if node == None:
            return
        if len(self.store_list)<=level:
            self.store_list.append([])
        self.store_list[level].append(node)
        self.pre_order_traversal(node.left,level+1)
        self.pre_order_traversal(node.right,level+1)


sol = Solution()

# input
[1,2,3,4,5,null,7]
[]
[1]
[1,2,3]
[1,2,3,null,1]

# output
output = sol.connect(root)
# answer
answer = ""
print(output, answer, answer == output)
