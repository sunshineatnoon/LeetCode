##############################   Solution   ###############################
# The basic idea is to first flat left sub-tree and return the last node, #
# then flat the right sub-tree and return the last node, at last move     #
# flattened left sub-tree to root.right and append flattened the right    #
# sub-tree to the last node of flattened left sub-tree.                   #
###########################################################################
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recursive(self,root):
        if(root == None):
            return root
        if(root.left == None and root.right == None):
            return root

        leftTail, rightTail = None, None
        if(root.right != None):
            rightTail = self.recursive(root.right)
        if(root.left != None):
            leftTail = self.recursive(root.left)
            tmp = root.right
            root.right = root.left
            leftTail.right = tmp
            root.left = None
            # If there's no right tree, the last node of this sub-tree should be
            # the last node of its left sub-tree.
            if(rightTail == None):
                rightTail = leftTail
        return rightTail

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.recursive(root)
