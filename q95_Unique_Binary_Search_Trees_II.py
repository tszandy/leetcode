from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *
from bisect import bisect_left

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        
        def generate_trees(l,r):
            if r-l<1:
                return []
            if r-l == 1:
                return [TreeNode(val=r,left = None,right = None)]
        
            return_list = []
            for i in range(l,r):
                l_1 = i
                r_1 = i+1
                left_possible = generate_trees(l,l_1)
                right_possible = generate_trees(r_1,r)
                if not left_possible:
                    for right in right_possible:
                        return_list.append(TreeNode(val = i+1,left = None,right = right))
                elif not right_possible:
                    for left in left_possible:
                        return_list.append(TreeNode(val = i+1,left = left,right = None))
                else:
                    for right in right_possible:
                        for left in left_possible:
                            return_list.append(TreeNode(val = i+1,left = left,right = right))
            return return_list
        return generate_trees(0,n)

sol = Solution()


# input
n = 1

# output
output = sol.generateTrees(n)
# answer
answer = [[1]]
print(output, answer, answer == output)

# input
n = 3

# output
output = sol.generateTrees(n)
# answer
answer = [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
print(output, answer, sorted(answer) == sorted(output))
