##########################   Solution I: Loop   ###################################
# For an array [a1,a2,...,aN], say that we know a permutation of [a1,a2,...,aN-1] #
# Then we can put aN at position 0,1,...,N-1 to get a new permutation of length N #
# We do this for all permutations of length N-1 to get all permutations of length #
# N. Thus the algorithm can be summaried as :                                     #
# For each number:                                                                #
#     For each permutation of numbers ahead this number:                          #
#         insert this number at position 0,1,...,N-1                              #
#     Update all permutations so far                                              #
###################################################################################
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        N = len(nums)
        permutes = [[]]
        for num in nums:
            new_permutes = []
            for permute in permutes:
                for j in range(0,len(permute)+1):
                    tmp  = permute[:j]+[num]+permute[j:]
                    new_permutes.append(tmp)
            permutes = new_permutes
        return permutes
##########################   Solution I: Recursion   ##############################
# For an array [a1,a2,...,aN], we first recursively get all permutations of       #
# [a1,a2,...,aN-1], then insert aN at position 0,1,...,N to get all permutations  #
# [a1,a2,...,aN]                                                                  #
###################################################################################
class Solution(object):
    def recursive(self,nums):
        if(len(nums) == 0):
            return []
        if(len(nums) == 1):
            return [nums]
        permutes = self.recursive(nums[:-1])
        new_permutes = []
        for permute in permutes:
            for i in range(len(permute)+1):
                tmp = permute[:i] + [nums[-1]] + permute[i:]
                new_permutes.append(tmp)
        return new_permutes

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.recursive(nums)
s = Solution()
print(s.permute([1,2,3,4]))
