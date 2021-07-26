from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left,bisect_right
from itertools import count

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        return self.merge_trees(root1,root2)
        
        
    def merge_trees(self,node_1,node_2):
        if node_1 != None and node_2!=None:            
            left = self.merge_trees(node_1.left,node_2.left)
            right = self.merge_trees(node_1.right,node_2.right)
            return TreeNode(val = node_1.val+node_2.val,left=left,right=right)
        elif node_1!=None:
            return node_1
        elif node_2!=None:
            return node_2
        else:
            return None

sol = Solution()

# input
root1 = [1,3,2,5]

root2 = [2,1,3,null,4,null,7]

# output
output = sol.mergeTrees(root1,root2)
# answer
answer = ""
print(output, answer, answer == output)

# input
root1 = [1]

root2 = [1,2]

# output
output = sol.mergeTrees(root1,root2)
# answer
answer = ""
print(output, answer, answer == output)
