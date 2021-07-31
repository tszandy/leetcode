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
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        self.return_list = []
        self.target_sum = targetSum
        self.path_sum(root,0,[])
        return self.return_list
        
    def path_sum(self,node,count_sum,target_list):
        count_sum+=node.val
        target_list.append(node.val)
        if node.left==None and node.right == None and count_sum == self.target_sum:
            self.return_list.append(list(target_list))
        if node.left !=None:
            self.path_sum(node.left,count_sum,target_list)
        if node.right !=None:
            self.path_sum(node.right,count_sum,target_list)
        target_list.pop()


sol = Solution()

# input
[5,4,8,11,null,13,4,7,2,null,null,5,1]
22
[1,2,3]
5
[1,2]
0
[]
0
# output
output = sol.pathSum(root,targetSum)
# answer
answer = ""
print(output, answer, answer == output)
