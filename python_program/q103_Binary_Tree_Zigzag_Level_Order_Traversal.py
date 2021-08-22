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
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        self.return_list = []
        if root == None:
            return self.return_list
        self.store_zig_zag = [root]
        self.left_to_right()
        return self.return_list
        
    def right_to_left(self):
        if self.store_zig_zag:
            next_store_list = []
            self.return_list.append([])
            for node in self.store_zig_zag:
                self.return_list[-1].append(node.val)
                if node.right!=None:
                    next_store_list.append(node.right)
                if node.left!=None:
                    next_store_list.append(node.left)
            self.store_zig_zag = next_store_list[::-1]
            self.left_to_right()
        else:
            return
        
    def left_to_right(self):
        if self.store_zig_zag:
            next_store_list = []
            self.return_list.append([])
            for node in self.store_zig_zag:
                self.return_list[-1].append(node.val)
                if node.left!=None:
                    next_store_list.append(node.left)
                if node.right!=None:
                    next_store_list.append(node.right)
            self.store_zig_zag = next_store_list[::-1]
            self.right_to_left()
        else:
            return
        

sol = Solution()

# input
[3,9,20,1,null,null,7,1,2,null,null,null,null,5,null]
[3,9,20,null,null,15,7]
[3,9,20,1,null,null,7]
[1]
[]
# output
output = sol.zigzagLevelOrder(root)
# answer
answer = ""
print(output, answer, answer == output)
