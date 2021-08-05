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
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root == None:
            return
        if root.val == key and root.left == root.right==None:
            return None
        self.delete_node(root,key)
        return root
        
        
    def delete_node(self,node,key):
        if node == None:
            return
        if key<node.val:
            self.delete_node(node.left,key)
        elif node.val > key:
            self.delete_node(node.right,key)
        elif node.val == key:
            if node.left !=None:
                node.val,node.left.val = node.left.val,node.val
                self.delete_node(node.left,key)
                if node.left.left == node.left.right == None:
                    node.left = None
            elif node.right !=None:
                node.val,node.right.val = node.right.val,node.val
                self.delete_node(node.right,key)
                if node.right.left == node.right.right == None:
                    node.right = None

sol = Solution()

# input
[5,3,6,2,4,null,7]
3
[5,3,6,2,4,null,7]
0
[]
0
[5,3,6,2,4,null,7]
5

# output
output = sol.func()
# answer
answer = ""
print(output, answer, answer == output)
