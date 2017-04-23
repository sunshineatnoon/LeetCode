################################   Solution   ###############################
# 123 = 1*100 + 2*10 + 3*1 = (1 + 99) + (2 + 9*2) + 3  -> 123%9 = 1+2+3 = 6 #
# N = a1*(10^(n-1)) + a2*(10^(n-2)) + ... + an -> N%9 = a1 + a2 +... + an   #
# So the solution is: num%9 if num%9 != 0; 9 if num%9 == 0                  #
#############################################################################
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if(num == 0):
            return num
        elif(num % 9 == 0):
            return 9
        else:
            return num%9
