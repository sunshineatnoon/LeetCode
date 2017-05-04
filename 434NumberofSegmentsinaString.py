class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        prev = ' '
        ans = 0
        hasNoneSpace = False
        for c in s:
            if(c != ' '):
                hasNoneSpace = True
            if(prev != ' ' and c == ' '):
                ans += 1
            prev = c
        if hasNoneSpace and prev != ' ':
            ans += 1
        return ans
