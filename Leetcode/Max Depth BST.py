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
        if root is not None:
            stack.append((1, root))

        depth = 0

        while stack:
            current_depth, current_tree_node = stack.pop()
            print current_tree_node.val
            depth = max(depth, current_depth)
            # doing left or right doesn't matter in this case cuz
            # we're only focused on depth
            if current_tree_node.left:
                stack.append((current_depth+1, current_tree_node.left))
            if current_tree_node.right:
                stack.append((current_depth+1, current_tree_node.right))

        return depth


    # You're basically including all the treenodes in the stack and evertime you "elevate down"
    # finding either a left/right bc that means theres more depth to the tree.
