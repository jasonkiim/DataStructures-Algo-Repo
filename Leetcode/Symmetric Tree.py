# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        return self.helperFunc(root.left, root.right)

    def helperFunc (self, node1, node2):

        if node1 == None and node2 == None:
            return True
        elif node1 and node2 and node1.val == node2.val and self.helperFunc(node1.left, node2.right) and self.helperFunc(node1.right, node2.left):
            return True
        else:
            return False
