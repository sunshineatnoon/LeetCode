#################   Native Solution   #################
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev = -1
        count = 0
        max_count = -1
        for num in nums:
            if(num ==1):
                if(prev == 1):
                    count += 1
                else:
                    max_count = max(count,max_count)
                    count = 1
            else:
                max_count = max(count,max_count)
                count = 0
            max_count = max(count,max_count)
            prev = num
        return max_count
        
#################   Simple Solution   #################
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        max_count = 0
        for num in nums:
            if(num == 1):
                count += 1
                max_count = max(max_count,count)
            else:
                count = 0
        return max_count
