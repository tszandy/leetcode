from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        return_list_node_pointer = None
        if l1 and l2:
            if l1.val<=l2.val:
                return_list_node_head = l1
                l1 = l1.next
            else:
                return_list_node_head = l2
                l2 = l2.next

            return_list_node_pointer = return_list_node_head
            while l1 and l2:
                if l1.val<=l2.val:
                    return_list_node_pointer.next = l1
                    return_list_node_pointer = return_list_node_pointer.next
                    l1 = l1.next
                else:
                    return_list_node_pointer.next = l2
                    return_list_node_pointer = return_list_node_pointer.next
                    l2 = l2.next
        if l1:
            if not return_list_node_pointer:
                return l1
            return_list_node_pointer.next = l1
            return return_list_node_head  
        if l2:
            if not return_list_node_pointer:
                return l2
            return_list_node_pointer.next = l2
            return return_list_node_head 
        return None 

sol = Solution()


# input

# output
output = sol.mergeTwoLists(l1,l2)
# answer
answer = ""
print(output, answer, answer == output)
