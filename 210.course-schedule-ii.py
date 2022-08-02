#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#
from functools import lru_cache
from lcimports import *
# @lc code=start
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # bfs
        graph = {i:[] for i in range(numCourses)}
        inedges = {i: 0 for i in range(numCourses)}
        for crs, pre in prerequisites:
            graph[pre].append(crs)
            inedges[crs] += 1
        
        # get all open courses
        queue = [i for i in inedges if inedges[i] == 0]
        courses_taken = []
        while queue:
            # take the course
            course = queue.pop(0)
            courses_taken.append(course)
            
            # reduce prerequisites for all dependencies
            for dependency in graph[course]:
                inedges[dependency] -= 1
                
                # add to queue if dependency has no more prerequisites
                if inedges[dependency] == 0:
                    queue.append(dependency)
        
        # check if all courses are taken
        if len(courses_taken) == numCourses:
            return courses_taken
        return []
        
# @lc code=end

