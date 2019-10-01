# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # Recursive approach
    def reverseList1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """


        if not head or not head.next:
            return head

        p = self.reverseList(head.next)
        # Let's say head is 4. Go from 4-> 5 to 5 -> 4 by setting next of 5 as 4. Then, set head.next as null to     accomplish linked list going backwards.
        head.next.next = head
        head.next = None

        return p

    # Iterative approach
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        prev = None
        current = head
        while current:
            actual_next = current.next
            current.next = prev
            prev = current
            current = actual_next

        # We return prev because at the end, the prev is at the end of the original linked list
        return prev
