# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        left = ListNode(0)
        output_left = left
        right = ListNode(0)
        output_right = right
        isEvenIndex = True

        while head:
            if not isEvenIndex:
                left.next = head
                left = left.next
            else:
                right.next = head
                right = right.next
            head = head.next
            isEvenIndex = not isEvenIndex

        # We need to define left.next as None explicitly otherwise it's pointing to a non-existing node.
        left.next = None
        right.next = output_left.next
        return output_right.next
