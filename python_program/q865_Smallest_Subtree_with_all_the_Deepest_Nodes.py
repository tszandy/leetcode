from typing import List
from collections import Counter,defaultdict,deque
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left,bisect_right
from itertools import count
import queue

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return root
        self.level = 0
        self.deepest_nodes = []
        self.recursive(root,1)
        if len(self.deepest_nodes)==1:
            return self.deepest_nodes[0]
        while not all(node == self.deepest_nodes[0] for node in self.deepest_nodes):
            self.deepest_nodes = map(lambda x:x.par,self.deepest_nodes)
        return self.deepest_nodes[0]
            
    def recursive(self,node,level,par=None):
        if node == None:
            return 
        node.par = par
        if self.level<level:
            self.level = level
            self.deepest_nodes = []
            self.deepest_nodes.append(node)
        elif self.level == level:
            self.deepest_nodes.append(node)
        self.recursive(node.left,level+1,node)
        self.recursive(node.right,level+1,node)

sol = Solution()

# input
[3,5,1,6,2,0,8,null,null,7,4]
[1]
[0,1,3,null,2]
[0,1,null,3,2,6,null,5,4]


# output
output = sol.func()
# answer
answer = ""
print(output, answer, answer == output)

