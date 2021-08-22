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
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        store_list = [root]
        level = 0
        while store_list:
            next_list = []
            if level%2 == 0:
                pre = float("-inf")
                for node in store_list:
                    if node.val%2!=1 or pre>=node.val:
                        return False
                    if node.left!=None:
                        next_list.append(node.left)
                    if node.right!=None:
                        next_list.append(node.right)
                    pre = node.val
            else:
                pre = float("inf")
                for node in store_list:
                    if node.val%2!=0 or pre<=node.val:
                        return False
                    if node.left!=None:
                        next_list.append(node.left)
                    if node.right!=None:
                        next_list.append(node.right)
                    pre = node.val
            store_list = next_list
            level+=1
        return True


sol = Solution()

# input
[1,10,4,3,null,7,9,12,8,6,null,null,2]
[5,4,2,3,3,7]
[5,9,1,3,5,7]
[1]
[11,8,6,1,3,9,11,30,20,18,16,12,10,4,2,17]

# output
output = sol.func()
# answer
answer = ""
print(output, answer, answer == output)
