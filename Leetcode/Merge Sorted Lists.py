# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        # Treat it as if you're declaring the head as the pointer 0 and you're appending l3 constantly. Then simply, return the listnodes starting @ position 1.

        head = ListNode(0)
        l3 = head

        #  Take care of the majority of the case
        while l1 and l2:
            if l1.val < l2.val:
                l3.next = l1
                l1 = l1.next
            else:
                l3.next = l2
                l2 = l2.next
            l3 = l3.next

        # Take care of the dangling case
        l3.next = l1 or l2
        return head.next
