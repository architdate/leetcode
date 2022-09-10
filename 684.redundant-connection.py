#
# @lc app=leetcode id=684 lang=python3
#
# [684] Redundant Connection
#
from lcimports import *
# @lc code=start
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = [i for i in range(len(edges) + 1)]
        ranks = [1] * (len(edges) + 1)

        def find(n):
            p = parents[n]
            while p != parents[p]:
                parents[p] = parents[parents[p]]
                p = parents[p]
            return p

        # False if same parent
        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)
            if p1 == p2:
                return False
            if ranks[p1] > ranks[p2]:
                parents[p2] = p1
                ranks[p1] += ranks[p2]
            else:
                parents[p1] = p2
                ranks[p2] += ranks[p1]
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
        
# @lc code=end

