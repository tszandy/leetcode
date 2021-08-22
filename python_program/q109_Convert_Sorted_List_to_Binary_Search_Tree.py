from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left,bisect_right
from itertools import count
import queue

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if head == None:
            return None
        return self.sorted_list_to_BST(head)
        
        
    def sorted_list_to_BST(self,node):
        if node == None:
            return None
        if node.next == None:
            return TreeNode(val = node.val)
        before_mid = node
        right = node
        if right.next!=None and right.next.next!=None:
            right = right.next.next
        while right.next!=None and right.next.next!=None:
            before_mid = before_mid.next
            right = right.next.next
        mid = before_mid.next
        before_mid.next = None
        left = self.sorted_list_to_BST(node)
        right = self.sorted_list_to_BST(mid.next)
        return TreeNode(val = mid.val,left = left,right=right)


sol = Solution()

# input
[]
[0]
[0, 1]
[0, 1, 2]
[0, 1, 2, 3]
[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4, 5]
[0, 1, 2, 3, 4, 5, 6]
[0, 1, 2, 3, 4, 5, 6, 7]
[0, 1, 2, 3, 4, 5, 6, 7, 8]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
[-10,-3,0,5,9]
[]
[0]
[1,3]
# output
output = sol.sortedListToBST(head)

# answer
answer = ""
print(output, answer, answer == output)
