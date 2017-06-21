###########################################################################
# Naive Solution: traverse every pair and record pairs with minimum index #
###########################################################################
class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        ans = {}
        minimum = 2010
        for i in range(len(list1)):
            for j in range(len(list2)):
                if(list1[i] == list2[j]):
                    if i+j < minimum:
                        minimum = i+j 
                    if((i+j) in ans):
                        ans[i+j].append(list1[i])
                    else:
                        ans[i+j] = [list1[i]]
        if(minimum == 1005):
            res = []
        else:
            res = ans[minimum]
        return res
###########################################################################
# Take advantage of Python's dictionary. Save list1 in a dictionary A,    #
# tranverse list2, see if each entry in list1 also appears in list2, if it#
# does, see if their summed index is smaller the best index so far.       #
###########################################################################
class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        ans = []
        minimum = 2010
        A = {u: i for i,u in enumerate(list1)}
        for j,v in enumerate(list2):
            if(v in A):
                i = A.get(v,2010)
                if(i+j < minimum):
                    minimum = i + j
                    ans = [v]
                elif(i+j == minimum):
                    ans.append(v)
        return ans
