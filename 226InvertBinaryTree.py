# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
##############################   Notes   ###############################
# You need to swap the whole left&right sub-tree, not just the values. #
########################################################################
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if(root != None):
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root
