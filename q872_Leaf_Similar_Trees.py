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
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        self.list_1 = []
        self.list_2 = []
        self.leaf_similar_1(root1)
        self.leaf_similar_2(root2)
        for i,j in zip_longest(self.list_1,self.list_2,fillvalue=None):
            if i !=j:
                return False
        return True
    def leaf_similar_1(self,node):
        if node == None:
            return
        if node.left==node.right==None:
            self.list_1.append(node.val)
        else:
            self.leaf_similar_1(node.left)
            self.leaf_similar_1(node.right)

    def leaf_similar_2(self,node):
        if node == None:
            return
        if node.left==node.right==None:
            self.list_2.append(node.val)
        else:
            self.leaf_similar_2(node.left)
            self.leaf_similar_2(node.right)

sol = Solution()

# input
[3,5,1,6,2,9,8,null,null,7,4]
[3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
[1]
[1]
[1]
[2]
[1,2]
[2,2]
[1,2,3]
[1,3,2]

# output
output = sol.func()
# answer
answer = ""
print(output, answer, answer == output)
