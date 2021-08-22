from typing import List
from collections import Counter,defaultdict,deque
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left,bisect_right
from itertools import count,zip_longest
import queue

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        current_list = [('',root)]
        smallest = None
        get_smallest = False
        while current_list:
            next_list = []
            for string,node in current_list:
                if node.left==node.right==None:
                    if smallest == None or chr(97+node.val)+string< smallest:
                        smallest = chr(97+node.val)+string
                if node.left!=None:
                    next_list.append((chr(97+node.val)+string,node.left))
                if node.right!=None:
                    next_list.append((chr(97+node.val)+string,node.right))
            current_list = next_list
        return smallest

sol = Solution()

# input
[0,1,2,3,4,3,4]
[25,1,3,1,3,0,2]
[2,2,1,null,1,0,null,0]
[0]
[1]
[0,1]
[3,9,20,null,null,15,7]

# output
output = sol.func()
# answer
answer = ""
print(output, answer, answer == output)
