# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        r_type = []
        queue = []

        if root is None:
            return
        queue.append(root)

        # You want to do a for loop after enqueing the necessary children to make sure they get added to r_type_contents
        # properly
        while len(queue):
            r_type_contents = []
            for _ in range(len(queue)):
                current = queue.pop(0)
                r_type_contents.append(current.val)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            r_type.append(r_type_contents)
        return r_type
