# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import random

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head_node = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        count = 0
        count += 1
        return_node = self.head_node
        next_node = self.head_node.next
        while next_node != None:
            count+=1
            if random.random()<=1.0/count:
                return_node = next_node
            next_node = next_node.next
        return return_node.val



# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
