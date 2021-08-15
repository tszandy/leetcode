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
        root = TreeNode(val = float("inf"),left = root)
        self.delete_node(root,key)
        return root.left
        
        
    def delete_node(self,node,key):
        if node == None:
            return
        if key<=node.val:
            if node.left!=None:
                if node.left.val == key:
                    if node.left.left==node.left.right==None:
                        node.left = None
                        return
                    elif node.left.left!=None:
                        delete_key = self.pre_elem(node.left.left)
                        node.left.val = delete_key
                        self.delete_node(node.left,delete_key)
                        return
                    else:
                        delete_key = self.post_elem(node.left.right)
                        node.left.val = delete_key
                        self.delete_node(node.left,delete_key)
                        return
                else:
                    self.delete_node(node.left,key)
        if key>=node.val:
            if node.right!=None:
                if node.right.val == key:
                    if node.right.left == node.right.right==None:
                        node.right = None
                        return
                    elif node.right.left!=None:
                        delete_key = self.pre_elem(node.right.left)
                        node.right.val = delete_key
                        self.delete_node(node.right,delete_key)
                    else:
                        delete_key = self.post_elem(node.right.right)
                        node.right.val = delete_key
                        self.delete_node(node.right,delete_key)
                        return
                else:
                    self.delete_node(node.right,key)

    def pre_elem(self, node):
        if node.right!=None:
            return self.pre_elem(node.right)
        else:
            return node.val
        
    def post_elem(self, node):
        if node.left!=None:
            return self.post_elem(node.left)
        else:
            return node.val

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
[2,1,3]
1
[2,1,3]
2
[2,1,3]
3
[2,1,3]
4

# output
output = sol.func()
# answer
answer = ""
print(output, answer, answer == output)
