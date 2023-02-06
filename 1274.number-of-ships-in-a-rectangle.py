#
# @lc app=leetcode id=1274 lang=python3
#
# [1274] Number of Ships in a Rectangle
#
from lcimports import *
class Sea:
   def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
    return True

class Point:
	def __init__(self, x: int, y: int):
		self.x = x
		self.y = y
# @lc code=start
# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea:
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point:
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution:
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        if (topRight.x < bottomLeft.x) or (topRight.y < bottomLeft.y):
            return 0
        if not sea.hasShips(topRight, bottomLeft):
            return 0
        if topRight.x == bottomLeft.x and topRight.y == bottomLeft.y:
            return 1
        mpx, mpy = (topRight.x + bottomLeft.x) // 2, (topRight.y + bottomLeft.y) // 2
        return self.countShips(sea, Point(mpx, mpy), bottomLeft) + \
               self.countShips(sea, Point(topRight.x,  mpy), Point(mpx + 1, bottomLeft.y)) + \
               self.countShips(sea, Point(mpx, topRight.y), Point(bottomLeft.x, mpy + 1)) + \
               self.countShips(sea, topRight, Point(mpx+1, mpy+1))
        
# @lc code=end

