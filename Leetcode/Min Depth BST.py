# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        stack = []
        lis = []
        min_depth = 0
        if root is not None:
            stack.append((1, root))
        else:
            return 0

        while stack:
            current_depth, current_node = stack.pop()
            print (current_node.val)
            if current_node.left:
                stack.append((current_depth+1, current_node.left))
            if current_node.right:
                stack.append((current_depth+1, current_node.right))

            if not current_node.left and not current_node.right:
                lis.append(current_depth)

        lis.sort()
        if lis is None:
            return 0
        else:
            return lis[0]

# Need to figure out how to keep t track of the depth at all times and return
# it at the end rather than placing them in an extra data structure...
