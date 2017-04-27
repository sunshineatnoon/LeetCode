###############################   Using Dictionary   ######################################
# 1. Go through the string and count each characters frequency, save it in a dictionary,  #
#    with key to be each character, value to be the frequency of this character.          #
# 2. Go through the frequency dictionary, and build a list of lists, the ith list contains#
#    all characters that appear i times in the string.                                    #
# 3. Go through the list of lists reversely and append each character n times, n is the   #
#    index of the list in the big list.                                                   #
###########################################################################################
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        c2n = {}
        maxx = 0
        for c in s:
            c2n[c] = c2n.get(c,0) + 1
            maxx = max(maxx, c2n[c])
        n2c = [[] for i in range(maxx+1)]

        for k,v in c2n.iteritems():
            n2c[v].append(k)
        ans = ""
        for i in range(maxx,0,-1):
            if(n2c[i] > 0):
                for c in n2c[i]:
                    ans += c*i
        return ans

###############################   Using Hash Table   ########################################
# Counter: A Counter is a dict subclass for counting hashable objects                       #
# Counter.most_common(): Return a list of the n most common elements and their counts from  #
# the most common to the least. If n is omitted or None, most_common() returns all elements #
# in the counter. Elements with equal counts are ordered arbitrarily                        #
#############################################################################################
from collections import Counter
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        cnt = Counter(s)
        cnt2 = cnt.most_common()
        ans = ""
        for kv in cnt2:
            ans += kv[0]*kv[1]
        return ans

s = Solution()
print(s.frequencySort("Aabb"))
