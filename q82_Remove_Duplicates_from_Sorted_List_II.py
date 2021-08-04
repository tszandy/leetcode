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
        head = ListNode(val = None,next = head)
        node = head
        while node.next!=None:
            if node.next!=None and node.next.next!=None:
                node_1_next = node.next
                node_2_next = node.next.next
                if node_1_next.val == node_2_next.val:
                    if node.next.next.next!=None:
                        node_3_next = node.next.next.next
                        if node_1_next.val == node_2_next.val==node_3_next.val:
                            node_1_next.next = node_2_next.next
                        else:
                            node.next = node_3_next
                    else:
                        node.next = None
                else:
                    node = node.next
            else:
                node = node.next
                continue
        return head.next


sol = Solution()

# input
[1,2,3,3,4,4,5]
[1,1,1,2,3]
[1,1]
[]
# output
output = sol.deleteDuplicates(head)
# answer
answer = ""
print(output, answer, answer == output)
