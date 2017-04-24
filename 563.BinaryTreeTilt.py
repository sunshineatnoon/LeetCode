# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def __init__(self):
        self.tiltSum = 0
        
    def NodeSum(self,root):
        """
        recursively calculate sum of each node
        """
        if(root == None):
            return 0,0
        leftSum,leftTilt = self.NodeSum(root.left)
        rightSum,rightTilt = self.NodeSum(root.right)
        self.tiltSum += leftTilt
        self.tiltSum += rightTilt
        return [leftSum + rightSum + root.val, abs(leftSum - rightSum)]
        
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        s, t = self.NodeSum(root)
        return self.tiltSum + t
        
        
