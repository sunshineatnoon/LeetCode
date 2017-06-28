#################################################################################################
# Solution: DP. For each element in nums nums[i], matain a longest list lists[i] that satisfies #
the requirements and ends with nums[i]. Initial setup are lists with sublists each only contains#
# nums[i]. Then loop over nums, and see if nums[j] can be append to any matained lists prior to #
# lists[j]. If it can be appended and gets a longer list after appending then update lists[j].  #
#################################################################################################
class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if(n == 0):
            return []
        else:
            nums.sort()
        lengths = [1 for i in range(n)]
        lists = [[nums[i]] for i in range(n)]
        
        for i in range(1,n):
            for j in range(i-1,-1,-1):
                if(nums[i] % nums[j] == 0):
                    if(lengths[i] < lengths[j] + 1):
                        lists[i] = lists[j] + [nums[i]]
                        lengths[i] = lengths[j] + 1
        
        maxx = 0
        res = []
        for i in range(n):
            if(lengths[i] > maxx):
                res = lists[i]
                maxx = lengths[i]
        
        return res
