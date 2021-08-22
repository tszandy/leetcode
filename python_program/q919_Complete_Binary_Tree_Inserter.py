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
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        self.q = []
        if root == None:
            return
        self.node_list = [root]
        while self.node_list:
            next_list = []
            for node in self.node_list:
                if node.left==None or node.right == None:
                    self.q.append(node)
                if node.left!=None:
                    next_list.append(node.left)
                if node.right!=None:
                    next_list.append(node.right)
            self.node_list = next_list

    def insert(self, val):
        """
        :type val: int
        :rtype: int
        """
        if self.q[0].left!=None and self.q[0].right!=None:
            self.q.pop(0)
        if self.q[0].left==None:
            self.q[0].left = TreeNode(val = val)
            self.q.append(self.q[0].left)
            return self.q[0].val
        else:
            self.q[0].right = TreeNode(val = val)
            self.q.append(self.q[0].right)
            return self.q[0].val

    def get_root(self):
        """
        :rtype: TreeNode
        """
        return self.root    


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()

sol = Solution()

# input
["CBTInserter","insert","insert","get_root"]
[[[1,2]],[3],[4],[]]
["CBTInserter","insert","insert","get_root"]
[[[1]],[3],[4],[]]
["CBTInserter","insert","insert","get_root"]
[[[1,2,3,4,5,6,7,8,9,10]],[3],[4],[]]

# output
output = sol.func()
# answer
answer = ""
print(output, answer, answer == output)
