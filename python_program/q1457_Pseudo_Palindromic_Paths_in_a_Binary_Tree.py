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
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.counter = Counter()
        self.count_palin = 0
        self.recursive(root)
        
        return self.count_palin
        

        
    def recursive(self,node):
        if node == None:
            return
        self.counter[node.val]+=1
        if node.left==node.right==None:
            self.check_palindrome()
        else:
            self.recursive(node.left)
            self.recursive(node.right)
        self.counter[node.val]+=1

        
        
    def check_palindrome(self):
        count_single = 0
        for val in self.counter.values():
            if val%2==1:
                count_single+=1
            if count_single>=2:
                return
        self.count_palin +=1

sol = Solution()

# input
[2,3,1,3,1,null,1]
[2,1,1,1,3,null,null,null,null,null,1]
[9]

# output
output = sol.pseudoPalindromicPaths(root)
# answer
answer = ""
print(output, answer, answer == output)
