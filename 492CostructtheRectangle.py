import math
class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        width = math.floor(math.sqrt(area))
        while(True):
           length = area/width
           if(length == math.floor(length)):
               return [int(length),int(width)]
           width -= 1
