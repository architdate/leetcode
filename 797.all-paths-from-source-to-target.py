#
# @lc app=leetcode id=797 lang=python3
#
# [797] All Paths From Source to Target
#
from lcimports import *
# @lc code=start
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        def dfs(node, prev):
            if node == len(graph) - 1:
                ans.append(prev + [node])
                return
            for n in graph[node]:
                dfs(n, prev + [node])
        dfs(0, [])
        return ans
        
# @lc code=end

