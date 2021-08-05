from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left,bisect_right
from itertools import count
import queue

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        self.store_list = []
        self.width_of_binary_tree(root,0,0)
        return max(map(lambda x:x[1]-x[0]+1,self.store_list))
    def width_of_binary_tree(self,node,level,val):
        if node == None:
            return
        if len(self.store_list)<=level:
            self.store_list.append((val,val))
        else:
            min_val ,max_val = self.store_list[level]
            self.store_list[level] = (min(min_val,val),max(max_val,val))
        self.width_of_binary_tree(node.left,level+1,val*2)
        self.width_of_binary_tree(node.right,level+1,val*2+1)

sol = Solution()

# input
[1,3,2,5,3,null,9]
[1,3,null,5,3]
[1,3,2,5]
[1,3,2,5,null,null,9,6,null,null,7]

# output
output = sol.widthOfBinaryTree(root)
# answer
answer = ""
print(output, answer, answer == output)
