#
# @lc app=leetcode id=554 lang=python3
#
# [554] Brick Wall
#
from lcimports import *
# @lc code=start
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        edges = defaultdict(int)
        for w in wall:
            curr = 0
            for b in w:
                curr += b
                edges[curr] += 1
        edges[sum(wall[0])] = -1
        return len(wall) - max(max(edges.values()), 0)
        
# @lc code=end

