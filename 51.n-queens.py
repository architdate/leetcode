#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#
from lcimports import *
# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        rows_set, cols_set = set(), set()
        diag_set, rev_diag_set = set(), set()
        def backtrack(r, c, q, board):
            if q == 0:
                ans.append([''.join(x) for x in board])
                return
            if c == n:
                backtrack(r+1, 0, q, board)
                return
            if r == n:
                return
            valid = (r not in rows_set) and \
                    (c not in cols_set) and \
                    (r + c not in diag_set) and \
                    (r - c not in rev_diag_set)
            if valid:
                board[r][c] = 'Q'
                rows_set.add(r)
                cols_set.add(c)
                diag_set.add(r + c)
                rev_diag_set.add(r - c)
                if q == 1:
                    backtrack(r, c, 0, board)
                else:
                    backtrack(r+1, 0, q-1, board)
                board[r][c] = '.'
                rows_set.remove(r)
                cols_set.remove(c)
                diag_set.remove(r + c)
                rev_diag_set.remove(r - c)
            backtrack(r, c+1, q, board)
        backtrack(0, 0, n, [['.']*n for _ in range(n)])
        return ans
            
        
# @lc code=end

