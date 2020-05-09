# You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. 
# Check if these points make a straight line in the XY plane.

class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        def collinear(x1, y1, x2, y2, x3, y3): 
            if ((y3 - y2)*(x2 - x1) == (y2 - y1)*(x3 - x2)) :
                return True
            else:
                return False
        
        for i in range(2, len(coordinates)):
            if not collinear(coordinates[0][0], coordinates[0][1],
                            coordinates[1][0], coordinates[1][1],
                            coordinates[i][0], coordinates[i][1]):
                return False
        return True
