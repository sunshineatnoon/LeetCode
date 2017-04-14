##############################   Native Solution   #########################
#                          check 1~n one by one                            #
# 92 ms/38.02%                                                             #
############################################################################
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        for i in range(1,n+1):
            if(i%15 == 0):
                ans.append("FizzBuzz")
            elif(i%3 == 0):
                ans.append("Fizz")
            elif(i%5 == 0):
                ans.append("Buzz")
            else:
                ans.append(str(i))
        return ans
##########################   Solution II: two pointers   ##########################
# maintain two pointer, one is change from 3,6,..., the other changes from 5,     #
# 10..., then check if i equals to these two pointers and update them accordingly #
# 112 ms/14.44%                                                                   #
###################################################################################
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        fizz = 3
        buzz = 5
        ans = []
        for i in range(1,n+1):
            if(i == fizz and i == buzz):
                ans.append('FizzBuzz')
                fizz += 3
                buzz += 5
            elif(i == fizz):
                ans.append('Fizz')
                fizz += 3
            elif(i == buzz):
                ans.append('Buzz')
                buzz += 5
            else:
                ans.append(str(i))
        return ans
###########################   Solution III: two mods   ########################
# one thing to remember: empty string or string = string                      #
#                                72 ms/95.55%                                 #
###############################################################################
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        for i in range(1,n+1):
            ans.append('Fizz'*(i%3) + 'Buzz'*(i%5) or str(i))
        return ans
s = Solution()
print(s.fizzBuzz(15)))
