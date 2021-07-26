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
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        self.leaf_set = set()
        self.remove_leaf_nodes(root,target)
        if root.left == None and root.right == None and root.val == target:
            return None
        return root

    def remove_leaf_nodes(self,node,target):
        if node == None:
            return
        self.remove_leaf_nodes(node.left,target)
        self.remove_leaf_nodes(node.right,target)
        if node.left in self.leaf_set:
            self.leaf_set.remove(node.left)
            node.left = None
        if node.right in self.leaf_set:
            self.leaf_set.remove(node.right)
            node.right = None
        if node.left == None and node.right == None and node.val == target:
            self.leaf_set.add(node)

sol = Solution()

# input
[1,2,3,2,null,2,4]
2
[1,3,3,3,2]
3
[1,2,null,2,null,2]
2
[1,1,1]
1
[1,2,3]
1
[1,1]
1
[1]
1
# output
output = sol.removeLeafNodes(root,target)
# answer
answer = ""
print(output, answer, answer == output)
