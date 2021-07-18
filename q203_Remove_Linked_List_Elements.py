from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache
import numpy as np
from heapq import *
from bisect import bisect_left

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while head and head.val == val:
            head = head.next
        if head == None:
            return head
        pre = head
        
        while pre.next:
            if pre.next.val == val:
                pre.next = pre.next.next
            else:
                pre = pre.next
        return head        

sol = Solution()


# input
[1,2,6,3,4,5,6]
6
[]
1
[7,7,7,7]
7
[2]
1
# output
output = sol.func()
# answer
answer = ""
print(output, answer, answer == output)
