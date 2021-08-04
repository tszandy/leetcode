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
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        next_node = head
        while next_node.next !=None:
            if next_node.next.val == next_node.val:
                next_node.next = next_node.next.next
            else:
                next_node = next_node.next
        return head

sol = Solution()

# input
[]
[1]
[1,1]
[1,1,2]
[1,1,2,3,3]

# output
output = sol.func()
# answer
answer = ""
print(output, answer, answer == output)
