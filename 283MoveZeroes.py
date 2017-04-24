class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        pointer = 0
        for num in nums:
            if(num != 0):
                nums[pointer] = num
                pointer += 1
        while(pointer < len(nums)):
            nums[pointer] = 0
            pointer += 1
