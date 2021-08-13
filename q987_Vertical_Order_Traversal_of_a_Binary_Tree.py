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
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.vertical_list_by_col_row = defaultdict(list)
        self.vertical_list_by_col = defaultdict(list)
        self.vertical_traversal(root)
        [i.sort() for i in self.vertical_list_by_col_row.values()]
        for col,row in sorted((self.vertical_list_by_col_row.keys()),key = lambda x:(x[0],x[1])):
            self.vertical_list_by_col[col]+=self.vertical_list_by_col_row[col,row]
        return list(map(lambda x:self.vertical_list_by_col[x],self.vertical_list_by_col.keys()))

    def vertical_traversal(self,node,row=0,col=0):
        if node == None:
            return
        self.vertical_list_by_col_row[col,row].append(node.val)
        self.vertical_traversal(node.left,row+1,col-1)
        self.vertical_traversal(node.right,row+1,col+1)

    def verticalTraversal_1(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.vertical_list = defaultdict(list)
        current_list = [(0,0,root)]
        while current_list:
            next_list = []
            for row,col,node in current_list:
                if self.vertical_list[col] and self.vertical_list[col][-1][0]==row and node.val < self.vertical_list[col][-1][1]:
                    self.vertical_list[col].insert(-1,(row,node.val))
                else:
                    self.vertical_list[col].append((row,node.val))
                if node.left!=None:
                    next_list.append((row+1,col-1,node.left))
                if node.right!=None:
                    next_list.append((row+1,col+1,node.right))
            current_list = next_list
        return list(map(lambda x:list(map(lambda y:y[1],self.vertical_list[x])),sorted(self.vertical_list.keys())))


sol = Solution()

# input
[3,9,20,null,null,15,7]
[1,2,3,4,5,6,7]
[1,2,3,4,6,5,7]
[3,1,4,0,2,2]
[0,8,1,null,null,3,2,null,4,5,null,null,7,6]
[0,2,1,3,null,5,22,9,4,12,25,null,null,13,14,8,6,null,null,null,null,null,27,24,26,null,17,7,null,28,null,null,null,null,null,19,null,11,10,null,null,null,23,16,15,20,18,null,null,null,null,null,21,null,null,29]

# output
output = sol.func()
# answer
answer = ""
print(output, answer, answer == output)
