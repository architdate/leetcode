#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#
from lcimports import *
# @lc code=start
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        pq = [(0, c) for c in range(COLS)] + [(r, 0) for r in range(1, ROWS)]
        pacifics = set(pq)
        while pq:
            r, c = pq.pop(0)
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS:
                    continue
                if (nr, nc) in pacifics or heights[nr][nc] < heights[r][c]:
                    continue
                pacifics.add((nr, nc))
                pq.append((nr, nc))
        aq = [(ROWS-1, c) for c in range(COLS)] + [(r, COLS-1) for r in range(ROWS-1)]
        atlantics = set(aq)
        while aq:
            r, c = aq.pop(0)
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS:
                    continue
                if (nr, nc) in atlantics or heights[nr][nc] < heights[r][c]:
                    continue
                atlantics.add((nr, nc))
                aq.append((nr, nc))
        return [list(x) for x in pacifics.intersection(atlantics)]
        
# @lc code=end

