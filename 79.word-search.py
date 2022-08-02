#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#
from lcimports import *
# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        visited = set()
        def dfs(r, c, i):
            if i == len(word) - 1 and board[r][c] == word[i]:
                return True
            if board[r][c] != word[i]:
                return False
            visited.add((r, c))
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= len(board) or nc < 0 or nc >= len(board[0]):
                    continue
                if (nr, nc) in visited:
                    continue
                if dfs(nr, nc, i + 1):
                    return True
            visited.remove((r, c))
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r, c, 0):
                    return True
        return False
        
# @lc code=end

