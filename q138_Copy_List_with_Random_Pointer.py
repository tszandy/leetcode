from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce,lru_cache,total_ordering
import numpy as np
from heapq import *
from bisect import bisect_left,bisect_right
from itertools import count
import queue

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None:
            return None
        self.copy_1_to_copy_2 = {None:None}
        head_2 = Node(x = head.val,next = None,random = None)
        self.copy_list(head,head_2)
        self.copy_random(head,head_2)
        return head_2

    def copy_list(self,head_1,head_2):
        self.copy_1_to_copy_2[head_1]=head_2
        if head_1.next!=None:
            head_2.next = Node(x=head_1.next.val,next = None,random = None)
            self.copy_list(head_1.next,head_2.next)

    def copy_random(self,head_1,head_2):
        if head_1!=None:
            head_2.random = self.copy_1_to_copy_2[head_1.random]
            self.copy_random(head_1.next,head_2.next)

sol = Solution()

# input
[[7,null],[13,0],[11,4],[10,2],[1,0]]
[[1,1],[2,1]]
[[3,null],[3,0],[3,null]]
[]

# output
output = sol.copyRandomList(head)
# answer
answer = ""
print(output, answer, answer == output)
