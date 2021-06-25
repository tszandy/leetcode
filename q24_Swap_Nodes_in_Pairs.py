from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        first = head
        second = head.next
        if first != None and second != None:
            first.next  = second.next
            second.next = first
            head = second
        while first.next!=None and first.next.next!=None:
            second = first.next
            first.next = second.next
            first = first.next
            second.next = first.next
            first.next = second
            swap = first
            first = second
            second = swap
            
        return head

sol = Solution()


# input

# output
output = sol.func()
# answer
answer = ""
print(output, answer, answer == output)
