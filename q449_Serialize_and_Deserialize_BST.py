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
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.store_serialize_result = []
        self.store_serialize_queue = queue.Queue()
        self.store_serialize_queue.put(root)
        while self.store_serialize_queue.qsize():
            node = self.store_serialize_queue.get()
            self.serialize_recurse(node)
        while len(self.store_serialize_result)>0 and self.store_serialize_result[-1]=="null":
            self.store_serialize_result.pop()
        return ",".join(self.store_serialize_result)
    
    def serialize_recurse(self,node):
        if node !=None:
            self.store_serialize_result.append(str(node.val))
            self.store_serialize_queue.put(node.left)
            self.store_serialize_queue.put(node.right)        
        else:
            self.store_serialize_result.append("null")
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data)==0:
            return None
        data_list = data.split(",")
        n = len(data_list)
        store_deserialize_queue = queue.Queue()
        root = TreeNode(data_list[0])
        store_deserialize_queue.put(root)
        i = 1
        while i < n:
            node = store_deserialize_queue.get()
            if data_list[i]!="null":
                node.left = TreeNode(int(data_list[i]))
                store_deserialize_queue.put(node.left)
            if i+1<n and data_list[i+1]!="null":
                node.right = TreeNode(int(data_list[i+1]))
                store_deserialize_queue.put(node.right)
            i+=2
        return root
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans

sol = Solution()

# input
[2,1,3]
[2,1,4,null,null,3,5]

# output
output = sol.func()
# answer
answer = ""
print(output, answer, answer == output)
