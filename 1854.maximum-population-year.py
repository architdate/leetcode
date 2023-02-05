#
# @lc app=leetcode id=1854 lang=python3
#
# [1854] Maximum Population Year
#
from lcimports import *
# @lc code=start
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        dates = []
        for birth, death in logs:
            dates.append((birth, 1))
            dates.append((death, -1))
            
        dates.sort()

        population = max_population = max_year = 0
        for year, change in dates:
            population += change
            if population > max_population:
                max_population = population
                max_year = year
        
        return max_year
        
# @lc code=end

