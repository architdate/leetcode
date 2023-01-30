#
# @lc app=leetcode id=735 lang=python3
#
# [735] Asteroid Collision
#
from lcimports import *
# @lc code=start
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []
        for a in asteroids:
            if a > 0:
                s.append(a)
            else:
                while s and s[-1] > 0 and abs(a) > s[-1]:
                    s.pop()
                if len(s) == 0 or s[-1] < 0:
                    s.append(a)
                if s[-1] == abs(a):
                    s.pop()
        return s
        
# @lc code=end

