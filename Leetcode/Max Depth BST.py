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
        """

        stack = []

        depth = 0

        if root is not None:
            stack.append((1, root))

        while stack:
            current_depth, current_node = stack.pop()
            depth = max(depth, current_depth)
            if current_node.left:
                stack.append((current_depth+1, current_node.left))
            if current_node.right:
                stack.append((current_depth+1, current_node.right))

        return depth
    # You're basically including all the treenodes in the stack and evertime you "elevate down"
    # finding either a left/right bc that means theres more depth to the tree.
    # Note that the tree structure is maintained in the input. This means that you can accss node.left
    # and node.right (if it exists).
    # Note that we're interested in the maximum "Depth". So we choose to use the "current_depth" and the existing value
    # of depth to compare the maximum. Then return the depth at the end of the while loop.



"""
Solution 2: Recursion
"""

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

        Lets understand the recursive formula. We know that the return type
        of this function is int, which means everytime we call this func recursively,
        we want to increment by one.

        So call maxDepth(root.left) and maxDepth(root.right), then get the maximum between the two
        """
        if root is None:
            return 0

        a = self.maxDepth(root.left)+1
        b = self.maxDepth(root.right)+1

        return max(a,b)
