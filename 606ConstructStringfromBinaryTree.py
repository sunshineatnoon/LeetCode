######################################################################
# Solution:                                                          #
# Travel the tree pre-order and process left, right node recursively #
######################################################################

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recursive(self,s,t):
        """
        : str: string so far
        : t: TreeNode
        """
        # Add root to string
        if t is None:
            return s
        elif(t.left is None and t.right is None):
            return s + '(' + str(t.val) + ')'
        else:
            s = s + '(' + str(t.val)
            
        # Left Node
        if t.left is None:
            s = s + '()'
        else:
            s = self.recursive(s, t.left)
        
        # Right Node
        if t.right is None:
            return s + ')'
        else:
            s = self.recursive(s, t.right)
        return s + ')'
        
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        s = self.recursive("", t)
        if(len(s) > 0):
            s = s[1:-1]
        return s
        
#######################################################################
# : super elegant and concise solution                                #
# The basic fact is that the format is root(left tree)(right tree),   # 
# if right tree is not empty while left tree is, we need to construct # 
# the string as root()(right tree).                                   #
# This gives this super simple code using Python formatting           #
#######################################################################

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t:
            return ''
        left = '({})'.format(self.tree2str(t.left)) if(t.left or t.right) else ''
        right = '({})'.format(self.tree2str(t.right)) if(t.right) else ''
        return '{}{}{}'.format(t.val,left,right)
