################ Naive Solution ################
#          Time Taken: 132 ms/31.12%           #
################################################
'''
class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for num in findNums:
            idx = nums.index(num)
            greater = -1
            for j in range(idx+1,len(nums)):
                if(nums[j] > num):
                    greater = nums[j]
                    break
            ans.append(greater)
        return ans
'''
################################  Solution II  #####################################
# maintain a stack which contains a decreasing squence. Then we see a number A     #
# larger than the last value of this squence, we pop elements less than this       #
# A, and these values' greater number is A. For instance, if the squence is        #
# [9 8 7 3 2 1 6], then the process goes like this:                                #
# 1. stack = [9]                                                                   #
# 2. 8 < stack[-1], append 8 to stack, stack = [9,8]                               #
# 3. 7 < stack[-1], append 7 to stack, stack = [9, 8, 7]                           #
# 4. ... keep appending 3, 2, 1 to stack for the same reason, stack = [9,8,7,3,2,1]#
# 5. 6 > stack[-1], we start to pop elements less than 6 in stack, we pop 1, 2, 3  #
#    and their greater values are 6. we append 6 to stack, stack = [9, 8 ,7, 6]    #
#    dic = {1:6, 2:6, 3:6}                                                         #
# 6. we go over findNums with dic to get final answers                             #
#                                Time Taken: 89 ms/59.23%                          #
####################################################################################
class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        ans, stack, dic = [], [], {}
        for num in nums:
            if(len(stack) == 0):
                stack.append(num)
            elif(num < stack[-1]):
                stack.append(num)
            else:
                while stack and stack[-1] < num:
                    dic[stack[-1]] = num
                    stack.pop()
                stack.append(num)
        for num in findNums:
            if(dic.has_key(num)):
                ans.append(dic[num])
            else:
                ans.append(-1)
        return ans

s = Solution()
print(s.nextGreaterElement([3,9,1],[9,8,7,3,2,1,6]))
