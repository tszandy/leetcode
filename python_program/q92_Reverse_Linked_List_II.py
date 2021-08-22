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
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        head = ListNode(val = None,next = head)
        before_list_node = head
        for _ in range(left-1):
            before_list_node = before_list_node.next
        head_list_node = before_list_node.next
        tail_list_node = head_list_node 
        for _ in range(right-left):
            tail_list_node = tail_list_node.next
        after_list_node = tail_list_node.next
        
        
        self.reverse_list(head_list_node,right-left)
        before_list_node.next = tail_list_node
        head_list_node.next = after_list_node
        return head.next

    def reverse_list(self,node,level):
        if level == 0:
            return
        self.reverse_list(node.next,level-1)
        node.next.next = node

sol = Solution()

# input
[1,2,3,4,5,6,7,8,9]
1
9
[1,2,3,4,5,6,7,8,9]
2
9
[1,2,3,4,5,6,7,8,9]
1
8
[1,2,3,4,5]
2
4
[5]
1
1
# output
output = sol.func()
# answer
answer = ""
print(output, answer, answer == output)
