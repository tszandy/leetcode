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
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.store_list = self.create_list(root)
        self.n = len(self.store_list)
        self.index = 0

    def create_list(self,node):
        if node == None:
            return []
        return self.create_list(node.left)+[node.val]+self.create_list(node.right)

    def next(self) -> int:
        if self.hasNext():
            elem = self.store_list[self.index]
            self.index+=1
            return elem
        else:
            return None
    def hasNext(self) -> bool:
        return self.index<self.n


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

sol = Solution()

# input
["BSTIterator","next","next","hasNext","next","hasNext","next","hasNext","next","hasNext"]
[[[7,3,15,null,null,9,20]],[],[],[],[],[],[],[],[],[]]

# output
output = sol.func()
# answer
answer = ""
print(output, answer, answer == output)
