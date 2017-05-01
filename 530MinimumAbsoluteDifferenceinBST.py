#####################################################################################################
# Binary Search Tree: A binary search tree is a rooted binary tree, whose internal nodes each store #
# a key and each have two distinguished sub-trees, commonly denoted left and right. The tree        #
# additionally satisfies the binary search tree property, which states that the key in each node    #
# must be greater than or equal to any key stored in the left sub-tree, and less than or equal to   #
# any key stored in the right sub-tree.                                                             #
# So we traverse this tree in-order and compare each node and the node previous to it since minumum #
# have to be the absolute different bewteen adjcent nodes.                                          #
#####################################################################################################
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def __init__(self):
        self.minimum = float("inf")
        self.prev = None
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if(root == None):
            return
        self.getMinimumDifference(root.left)
        if(self.prev != None):
            self.minimum = min(abs(root.val - self.prev.val),self.minimum)
        self.prev = root
        self.getMinimumDifference(root.right)
        return self.minimum
