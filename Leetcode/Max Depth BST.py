# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int

        The base case in this problem is that when we know there's no leaf nodes associated
        with a root, then we know we're at the bottom, so we simply return 0. Otherwise, we
        know that there's a left/right child, which means there's another level associated.
        Hence why we add 1 as we call the recursive function again.
        Calculate the depth of each left/right child, and then return the maximum of two.

        """
        if root == None:
            return 0
        else:
            a = self.maxDepth(root.left)+1
            b = self.maxDepth(root.right)+1
            return max(a, b)
