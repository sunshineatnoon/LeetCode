#########################################   Solution: Bit Addition   ############################################
# Let's consider two decimal digits 179 + 543 = 722                                                             #
# We can calculate this addition like this:                                                                     #
#    1. calculate addition without carries: 179+543 = 612                                                       #
#    2. only consider carries: 179+543 = 011 -> 110                                                             #
#    3. so the final result is 612 + 110 = 722                                                                  #
# of course the second addition could have carries too, so the second addition is actually a recursive process. #
# As for binary addition, we can use the xor operation to do addition without carries and & operation to do     #
# addition only considering carries, and recursively add shifted carries and xor results.                       #
#                                                                                                               #
# One tricky thing about python is that its default integer type is long, so -1 in Python would look like       #
# 0xFFFFFFFFFFFFFFFF, but it looks like 0xFFFFFFFF in 32-bit format. The input given is in 32-bit format,       #
# Python will treat it as a huge positive number, so we have to use c_int32 to constraint a and b to be 32-bit  #
#################################################################################################################
import ctypes
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        a = ctypes.c_int32(a)
        b = ctypes.c_int32(b)
        # Recursion end condition: b is 0, i.e. no more carries
        if(b.value == 0):
            return a.value
        # First Step: Addition without carries
        xor = a.value ^ b.value
        # Second Step: Addition only considering carries, and left shift carries by 1
        carries = a.value & b.value
        carries = carries << 1
        # Third Step: Recursively calculate sum of xor and carries
        return self.getSum(xor,carries)
