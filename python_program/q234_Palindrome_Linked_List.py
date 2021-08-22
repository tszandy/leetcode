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
    def isPalindrome(self, head: ListNode) -> bool:
        first = [head]
        
        def recursion(node):
            if node:
                result = recursion(node.next)
                if result and first[0].val == node.val:
                    first[0] = first[0].next
                    return True
                else:return False
            else:
                return True
        return recursion(head)

sol = Solution()


# input
[1]
[1,2]
[1,2,2,1]
[1,2,2,2,1]
[1,2,3,2,1]
# output
output = sol.isPalindrome()
# answer
answer = ""
print(output, answer, answer == output)
