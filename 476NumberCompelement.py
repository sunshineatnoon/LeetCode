#####   Solution I: Naive Solution   #####
'''
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        binary = []
        res = 0
        while(num >0):
            binary.append(num%2)
            num = int(num/2)
        exp = 1
        print(binary)
        for b in binary:
            res = res + (1-b)*exp
            exp *= 2
        return res
'''
#########################   Solution II: Bit Operation   ##########################
# To get complement of A, just do A ^ (111..11), with the number of 1 equal to    #
# the number of bits of A. For instance, for 5 = (101), the complement of 5 is    #
# (101)^(111) = (010). Say A has N bits. Then the loop gives us a mask with (N+1) #
# 1s, then mask-1 gives N 1s, A^mask is the complement of A                       #
###################################################################################
class Solution(object):
    def findComplement(self, num):
        mask = 1
        while mask <= num:
            mask = mask << 1
        return num ^ (mask - 1)
s = Solution()
print(s.findComplement(2))
