from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache
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
    def allPossibleFBT(self, n: int) -> List[TreeNode]:
        dp = defaultdict(list)
        dp[1].append(TreeNode(0))
        
        def all_possible_FBT(n):
            if n %2 ==1:
                if len(dp[n])==0:
                    return_list = []
                    for l in range(1,n,2):
                        r = n-1-l
                        for left_node in all_possible_FBT(l):
                            for right_node in all_possible_FBT(r):
                                parent = TreeNode(0)
                                parent.left = left_node
                                parent.right = right_node
                                return_list.append(parent)
                    dp[n]=return_list
                    return dp[n]
                else:
                    return dp[n]
        return all_possible_FBT(n)

sol = Solution()


# input
n = 7

# output
output = sol.allPossibleFBT(n)
# answer
answer = ""
print(output, answer, answer == output)
