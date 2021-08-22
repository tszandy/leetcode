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
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:        
        end_pre_list_node = ListNode(next = head)
        head = end_pre_list_node

        def reverse_node(node,k):
            if k!=1:
                return_node = reverse_node(node.next,k-1)
                return_node.next = node
                return node
            else:
                return node

        def reverse_list(node,k):
            count_next = 0
            end_pre_list_node = node
            start_cur_list_node = node.next
            end_cur_list_node = node
            while end_cur_list_node.next and count_next<k:
                end_cur_list_node = end_cur_list_node.next
                count_next+=1
            if count_next == k:
                start_post_list_node = end_cur_list_node.next
                reverse_node(start_cur_list_node,k)
                start_cur_list_node, end_cur_list_node = end_cur_list_node, start_cur_list_node
                end_pre_list_node.next = start_cur_list_node
                end_cur_list_node.next = start_post_list_node
                reverse_list(end_cur_list_node,k)

        reverse_list(head,k)
        return head.next


sol = Solution()


# input
[1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5]
13
[1,2,3,4,5]
2
[1,2,3,4,5]
3
[1,2,3,4,5]
1
[1,2,3]
2
[1]
1
# output
output = sol.reverseKGroup()
# answer
answer = ""
print(output, answer, answer == output)
