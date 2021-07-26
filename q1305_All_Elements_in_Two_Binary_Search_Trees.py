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
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        list_1 = self.get_list_from_tree(root1)
        list_2 = self.get_list_from_tree(root2)
        print(list_1)
        print(list_2)
        n_1 = len(list_1)
        n_2 = len(list_2)
        l_1 = 0
        l_2 = 0
        return_list = []
        while l_1<n_1 and l_2<n_2:
            elem_1 = list_1[l_1]
            elem_2 = list_2[l_2]
            if elem_1<elem_2:
                return_list.append(elem_1)
                l_1 += 1
            else:
                return_list.append(elem_2)
                l_2 += 1
        return return_list+list_1[l_1:]+list_2[l_2:]
        
        
        
    def get_list_from_tree(self,node):
        if node == None:
            return []
        else:
            return self.get_list_from_tree(node.left)+[node.val]+self.get_list_from_tree(node.right)

sol = Solution()

# input
root1 = [2,1,4]

root2 = [1,0,3]

# output
output = sol.getAllElements(root1, root2)
# answer
answer = ""
print(output, answer, answer == output)

# input
root1 = [0,-10,10]

root2 = [5,1,7,0,2]

# output
output = sol.getAllElements(root1, root2)
# answer
answer = ""
print(output, answer, answer == output)

# input
root1 = []

root2 = [5,1,7,0,2]

# output
output = sol.getAllElements(root1, root2)
# answer
answer = ""
print(output, answer, answer == output)

# input
root1 = [0,-10,10]

root2 = []

# output
output = sol.getAllElements(root1, root2)
# answer
answer = ""
print(output, answer, answer == output)

# input
root1 = [1,null,8]

root2 = [8,1]

# output
output = sol.getAllElements(root1, root2)
# answer
answer = ""
print(output, answer, answer == output)
