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
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None:
            return False
        tortoise = head
        hare = head
        tortoise = tortoise.next
        if tortoise==None:
            return False
        tortoise = tortoise.next
        hare = hare.next

        while tortoise != hare:
            if tortoise==None:
                return False
            tortoise = tortoise.next
            if tortoise==None:
                return False
            tortoise = tortoise.next
            hare = hare.next
        else:
            return True

sol = Solution()

# input
[3,2,0,-4]
1
[1,2]
0
[1,2]
-1
[1]
-1
[]
-1

# output
output = sol.hasCycle(head)
# answer
answer = ""
print(output, answer, answer == output)
