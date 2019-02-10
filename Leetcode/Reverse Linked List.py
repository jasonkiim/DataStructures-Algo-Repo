# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        stack = []
        current_node = head
        l1 = ListNode(0)
        output_head = l1

        while current_node is not None:
            stack.append(current_node)
            current_node = current_node.next

        while stack:
            node = stack.pop()
            l1.next = ListNode(node.val)
            l1 = l1.next

        return output_head.next
