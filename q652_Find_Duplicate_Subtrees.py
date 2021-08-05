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
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        self.node_val_to_dumplicate = defaultdict(set)
        self.store_dumplicate_set = set()
        self.store_dumplicate = []
        self.tree_2_str(root)
        return self.store_dumplicate
        

    def tree_2_str(self,node):
        if node == None:
            return ""
        return_str = str(node.val)
        if node.left==node.right==None:
            return_str+=""
        else:
            return_str+="("+self.tree_2_str(node.left)+")"
            if node.right!=None:
                return_str+="("+self.tree_2_str(node.right)+")"
        if return_str in self.node_val_to_dumplicate[node.val]:
            if not return_str in self.store_dumplicate_set:
                self.store_dumplicate.append(node)
                self.store_dumplicate_set.add(return_str)
        else:
            self.node_val_to_dumplicate[node.val].add(return_str)
        return return_str

sol = Solution()

# input
[1,2,3,4,null,2,4,null,null,4]
[2,1,1]
[2,2,2,3,null,3,null]

# output
output = sol.func()
# answer
answer = ""
print(output, answer, answer == output)
