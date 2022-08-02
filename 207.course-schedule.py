#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#
from functools import lru_cache
from lcimports import *
# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        prereq = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)
        
        @lru_cache(None)
        def dfs(c):
            visited.add(c)
            for n in prereq[c]:
                if n in visited:
                    return False
                if not dfs(n):
                    return False
            visited.remove(c)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        
# @lc code=end

