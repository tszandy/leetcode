# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        if l2 == None:
            return l1

        total = l1.val + l2.val
        return_node = ListNode(total%10)
        if total>=10:
            return_node.next = self.addTwoNumbersCarry(l1.next,l2.next)
        else:
            return_node.next = self.addTwoNumbers(l1.next,l2.next)
        return return_node

    def addTwoNumbersCarry(self,l1,l2):
        if l1 == None and l2 == None:
            return ListNode(1)
        if l1 == None:
            return self.oneNumberCarry(l2)
        if l2 == None:
            return self.oneNumberCarry(l1)
        total = l1.val + l2.val + 1
        return_node = ListNode(total%10)
        if total>=10:
            return_node.next = self.addTwoNumbersCarry(l1.next,l2.next)
        else:
            return_node.next = self.addTwoNumbers(l1.next,l2.next)
        return return_node

    def oneNumberCarry(self,l1):
        if l1 == None:
            return ListNode(1)
        total = l1.val + 1
        return_node = ListNode(total%10)
        if total>=10:
            return_node.next = self.oneNumberCarry(l1.next)
        else:
            return_node.next=l1.next
        return return_node
