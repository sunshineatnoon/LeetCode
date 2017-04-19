class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        cnt = [0] * (len(nums)+1)
        for num in nums:
            cnt[num] += 1
        ans = []
        for i in range(1,len(nums)+1):
            if(cnt[i] == 0):
                ans.append(i)
        return ans
