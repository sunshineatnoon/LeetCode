##############################   Native Solution   #########################
# using dict to check if every character in a word maps to the same number #
# Time taken: 39 ms/77.38%
############################################################################
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        Row1 = ['q','w','e','r','t','y','u','i','o','p']
        Row2 = ['a','s','d','f','g','h','j','k','l']
        Row3 = ['z','x','c','v','b','n','m']
        dic = {}
        for a in Row1:
            dic[a] = 1
        for a in Row2:
            dic[a] = 2
        for a in Row3:
            dic[a] = 3
        ans = []
        for w in words:
            backup = w
            w = w.lower()
            isSameRow = True
            prev = dic[w[0]]
            for i in range(1,len(w)):
                if(prev != dic[w[i]]):
                    isSameRow = False
                    prev = dic[w[i]]
            if(isSameRow):
                ans.append(backup)
        return ans
##############################   Solution II: set   ##########################
# put each row in the keyboard into a set, if all characters in a word comes #
# from the same row, then the word should be a subset of a set of a row      #
# Time taken: 52ms/26.52%                                                    #
##############################################################################
class Solution(object):
    def findWords(self, words):
        ans = []
        Row1 = set('qwertyuiop')
        Row2 = set('asdfghjkl')
        Row3 = set('zxcvbnm')
        for word in words:
            w = set(word.lower())
            if w.issubset(Row1) or w.issubset(Row2) or w.issubset(Row3):
                ans.append(word)
        return ans
s = Solution()
print(s.findWords(["Hello", "Alaska", "Dad", "Peace"]))
