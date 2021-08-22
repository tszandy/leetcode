from typing import List
from collections import Counter,defaultdict
from math import *
from functools import reduce
import numpy as np
from heapq import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        hq = []
        n = len(lists)
        for i in range(n):
            sorted_list_node = lists[i]
            if sorted_list_node != None:
                heappush(hq,(sorted_list_node.val,i))
                lists[i] = sorted_list_node.next
        return_list_node_head = None
        if hq:  
            value,i = heappop(hq)
            return_list_node_head = return_list_node_next = ListNode(val = value)
            
            sorted_list_node = lists[i]
            if sorted_list_node:
                heappush(hq,(sorted_list_node.val,i))
                lists[i] = sorted_list_node.next
        
        while hq:
            value,i = heappop(hq)
            return_list_node_next.next = ListNode(val = value)
            return_list_node_next = return_list_node_next.next

            sorted_list_node = lists[i]
            if sorted_list_node:
                heappush(hq,(sorted_list_node.val,i))
                lists[i] = sorted_list_node.next
        
        
        
        return return_list_node_head

sol = Solution()


# input
lists = [[1,4,5],[1,3,4],[2,6]]
# output
output = sol.mergeKLists(lists)
# answer
answer = [1,1,2,3,4,4,5,6]
print(output, answer, answer == output)
