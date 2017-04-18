################################   Solution   ###################################
# There're only two things need to be known for this problem:                   #
# 1. Any number x ^ 0 = x                                                       #
# 2. Any number x ^ x = 0                                                       #
# Thus we set ans initially to 0, and xor it with each number in nums, ans will #
# be left to the single number because all paired numbers are "canceled" by xor #
#################################################################################
 class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for num in nums:
            ans = ans ^ num
        return ans
