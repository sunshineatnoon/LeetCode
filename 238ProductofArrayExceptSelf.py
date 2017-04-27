##################################   Solution   #####################################
# Every element partitions the array into two parts, a sub array left to this       #
# element and a sub array right to this element. As long as we know multiplication  #
# of elements left to it and multiplication of elements right to it, we know the    #
# answer. So we go through this array twice:                                        #
# 1. First time we calculate multiplication of elements left to i and save this     #
#    multiplication in the result array named ans.                                  #
# 2. Second time we go through the array from right to left and maintain a variable #
#    called right to save the multiplication of all right elements so far. Thus     #
#    each element's answer will be right * ans[i].                                  #
#####################################################################################

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans = [1]*n
        for i in range(0,n-1):
            ans[i+1] = ans[i] * nums[i]

        right = 1
        for i in range(n-1,-1,-1):
            ans[i] = ans[i] * right
            right = right * nums[i]
        return ans
s = Solution()
print(s.productExceptSelf([1,2,3,4]))
