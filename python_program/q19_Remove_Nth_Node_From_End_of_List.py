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
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        node_count = self.get_count(head)
        count_next = node_count-n-1
        if n == node_count:
            head = head.next
            return head
        pre_remove_node = head
        while count_next:
            pre_remove_node = pre_remove_node.next
            count_next-=1
        if n ==1:
            pre_remove_node.next = None
            return head
        pre_remove_node.next = pre_remove_node.next.next
        return head

    def get_count(self,node)->int:
        if node.next == None:
            return 1
        else:
            return self.get_count(node.next)+1

sol = Solution()


# input

# output
output = sol.func()
# answer
answer = ""
print(output, answer, answer == output)
