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
        inedges = defaultdict(list)
        outedges = defaultdict(list)
        for curr, pre in prerequisites:
            inedges[curr].append(pre)
            outedges[pre].append(curr)
        starts = [c for c in range(numCourses) if len(inedges[c]) == 0]
        if not starts:
            return False

        globalvisits = set()
        @lru_cache(None)
        def hasCycle(start):
            globalvisits.add(start)
            visited.add(start)
            for next in outedges[start]:
                if next in visited:
                    return True
                if hasCycle(next):
                    return True
            visited.remove(start)
            return False
            
        visited = set()
        for start in starts:
            if hasCycle(start):
                return False
        return len(globalvisits) == numCourses
        
# @lc code=end

