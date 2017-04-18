####################   My Solution   #####################
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if(len(word) <= 1):
            return True
        allUpper = (not word[1].islower())
        allLower = word[1].islower()
        for i in range(1,len(word)):
            if not word[i].islower():
                allLower = False
            else:
                allUpper = False
        if(not word[0].islower() and (allLower or allUpper)):
            return True
        elif(word[0].islower() and allLower):
            return True
        else:
            return False

####################   Pythonic Solution   #####################
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return word.islower() or word.isupper() or word.istitle()
####################   Tricky Solution   #######################
# Counting Capital character numbers N.                        #
# if N == 0 or N == len(word) or (word[0] is upper and N == 1) #
# Then the usage of capitals is right                          #
################################################################
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        cnt = 0
        for i in range(len(word)):
            if(word[i].isupper()):
                cnt += 1
        return (cnt == 0) or (cnt == len(word)) or (cnt == 1 and word[0].isupper())
s = Solution()
print(s.detectCapitalUse('FlaG'))
