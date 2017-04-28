##################################################################################
# We already know to use xor to solve this problem: given a list of numbers in   #
# all elements appear twice except one. In this problem, we have two numbers     #
# that appear only once. So we should find a way to seperate these two numbers.  #
# We know that the xor of these two nmbers > 0 and there's at least 1 bit of     #
# these two numbers will be different. So we find this bit and use this bit to   #
# seperate the list into two sub lists, the two numbers we are looking for have  #
# to be in different groups. And we can use xor to find them in each group. So   #
# the final solution will be:                                                    #
# 1. Loop through the list and calculate xor of two target numbers.              #
# 2. Find 1 bit that is 1 in the xor, the two target numbers must have different #
#    numbers at this bit.                                                        #
# 3. Split the list into two sub-lists using this special bit.                   #
# 4. Use xor operation to find unique number in each sub-list.                   #
##################################################################################
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = 0
        for num in nums:
            xor = xor ^ num
        base = 1
        while (xor & base == 0):
            base = base << 1
        xor1, xor2 = 0, 0
        for num in nums:
            if(num & base == 0):
                xor1 ^= num
            else:
                xor2 ^= num
        return [xor1, xor2]

s = Solution()
print(s.singleNumber([1,2,1,3,2,5]))
