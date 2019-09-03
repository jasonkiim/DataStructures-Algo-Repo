# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution(object):
#     def inorderTraversal(self, root):
#         """
#         :type root: TreeNode
#         :rtype: List[int]
#         """

        # Leverage the stack (append and pop).
        # Append to stack until the root -> root.left is none
        # Move the current to stack.pop() when the stack isn't empty but current is none (AKA no left node to check)
        # Append the current value to the rType list and move forward to current.right
        # If the stack and current are both empty, then break out of inifnite loop.
        # stack = []
        # rType = []
        # current = root
        # while True:
        #     if current is not None:
        #         stack.append(current)
        #         current = current.left
        #     elif stack:
        #         current = stack.pop()
        #         rType.append(current.val)
        #         current = current.right
        #     else:
        #         break
        # return rType

# We need a helper because when the function gets called recursively, rType gets cleared out.
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        rType = []
        self.helper(root, rType)
        return rType

    def helper(self, root, rType):
        if root:
            if root.left:
                self.helper(root.left, rType)
            rType.append(root.val)
            if root.right:
                self.helper(root.right, rType)

    
