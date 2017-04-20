####################   Solution I: Counting   ###################
# dictionary.get(key,default): return a value for the given key.#
# If key is not available, then returns default value.          #
#################################################################
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dic = {}
        for ch in s:
            dic[ch] = dic.get(ch, 0) + 1
        for ch in t:
            if(dic.get(ch,0) == 0):
                return ch
            dic[ch] -= 1

##########   Solution II: Bit Operation   ##########
##          ord(i): integer -> character          ##
##          chr(i): character -> integer          ##
####################################################
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        c = 0
        for ch in s:
            c = c ^ ord(ch)
        for ch in t:
            c = c ^ ord(ch)
        return chr(c)
