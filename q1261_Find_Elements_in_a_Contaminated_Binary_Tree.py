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
class FindElements:

    def __init__(self, root: TreeNode):
        self.root = root
        self.recover_tree(root,0)
    
    def recover_tree(self,node,val):
        if node == None:
            return
        node.val = val
        self.recover_tree(node.left,val*2+1)
        self.recover_tree(node.right,val*2+2)

    def find(self, target: int) -> bool:
        
        child_list = []
        while target != 0:        
            if target%2 == 0:
                child_list.append("right")
            else:
                child_list.append("left")
            target = (target-1)//2
        child_list = child_list[::-1]
        node = self.root
        for instruction in child_list:
            if instruction == "left":
                node = node.left
            else:
                node = node.right
            if node == None:
                return False
        return True
            
# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)

sol = Solution()

# input
["FindElements","find","find"]
[[[-1,null,-1]],[1],[2]]
["FindElements","find","find","find"]
[[[-1,-1,-1,-1,-1]],[1],[3],[5]]
["FindElements","find","find","find","find"]
[[[-1,null,-1,-1,null,-1]],[2],[3],[4],[5]]

# output
output = sol.func()
# answer
answer = ""
print(output, answer, answer == output)
