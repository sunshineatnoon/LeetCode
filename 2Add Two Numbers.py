# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        pointer1 = l1
        pointer2 = l2
        ans = None
        pointerans = ans
        while(pointer1 != None and pointer2 != None):
            if(pointerans == None):
                pointerans = ListNode((pointer1.val + pointer2.val + carry)%10)
                ans = pointerans
            else:
                pointerans.next = ListNode((pointer1.val + pointer2.val + carry)%10)
                pointerans = pointerans.next
                
            carry = int((pointer1.val + pointer2.val + carry)/10)
            pointer1 = pointer1.next
            pointer2 = pointer2.next
            
        while(pointer1 != None):
            pointerans.next = ListNode((pointer1.val + carry)%10)
            carry = int((pointer1.val + carry)/10)
            pointerans = pointerans.next
            pointer1 = pointer1.next
            
        while(pointer2 != None):
            pointerans.next = ListNode((pointer2.val + carry)%10)
            carry = int((pointer2.val + carry)/10)
            pointerans = pointerans.next
            pointer2 = pointer2.next
        
        if(carry != 0):
            pointerans.next = ListNode(carry)
            pointerans = pointerans.next
        return ans

########################################
# same solution, but more elegant code #
########################################
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        ans = p = ListNode(0)
        while l1 or l2 or carry:
            v1, v2 = 0, 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry,v = divmod(v1+v2+carry,10)   
            p.next = ListNode(v)
            p = p.next
        return ans.next
