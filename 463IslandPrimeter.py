##############################       Solution     ################################
# go through each element in grid, check if this element has a 1 in left, right, #
# up, down neighbor, if not, then the corresponding direction should be count    #
# into perimeter.                                                                #
#                            Time Taken: 306ms/65.11% ( O(mn))                   #
##################################################################################
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0
        h = len(grid)
        w = len(grid[0])
        for i in range(0,h):
            for j in range(0,w):
                if(grid[i][j] == 1):
                    left, right , up, down = 1, 1, 1, 1
                    if(i-1 >= 0):
                        up = 1-grid[i-1][j]
                    if(i+1 < h):
                        down = 1-grid[i+1][j]
                    if(j-1 >= 0):
                        left = 1-grid[i][j-1]
                    if(j+1 < w):
                        right = 1-grid[i][j+1]
                    ans += left + right + up + down
        return ans

s = Solution()
print(s.islandPerimeter([[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]
))
