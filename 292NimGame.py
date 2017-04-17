############################################   Solution   ###########################################
# When it's A's turn to pick stones, if the number of stones is 4k (k=1,2...), then A will loss.    #
# We can proof this by recursion. Say N is the number of stones when it's A's turn to pick up.      #
# Step 1. if N = 4, then A will lose                                                                #
# Step 2. Assume N = 4k (k=1,2...), A will lose.                                                    #
# Step 3. if N = 4(k+1), then: if A pick 1 stone, then B can pick 3 stones which left A 4k stones   #
#         in the next turn; if A pick 2 stones, then B can pick 2 stones which left A 4k stones     #
#         in the next turn; if A pick 3 stones, then B can pick 1 stones which left A 4k stones     #
#         in the next turn. Thus there's no way A will win if B choose the optimal solution.        #
# Step4. By the proof of recursion, we have that A can't win when it's  A's turn and the number of  #
#        stones are 4k (k = 1,2,...)                                                                #
# When N % 4 != 0, then A can either pick 1,2,3 stones, left B 4k stones to let B lose. So when     #
# N % 4 != 0, A will always win.                                                                    #
#####################################################################################################
class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return (n%4 != 0)
