#
# @lc app=leetcode id=1329 lang=python3
#
# [1329] Sort the Matrix Diagonally
#
from lcimports import *
# @lc code=start
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        # Store the matrix dimensions
        m = len(mat)
        n = len(mat[0])

        # Hash Map to store the diagonals. We will use a list
        # for now, but then heapify each list before taking them out.
        diagonals = defaultdict(list)

        # Insert values into the Hash Map.
        for row in range(m):
            for col in range(n):
                # Observing that on each diagonal, the differences between the row and column indices
                # of each element is the same.
                # Hence we can use row - col as the key to collect elements on the same diagonal.
                diagonals[row - col].append(mat[row][col])
                
        # Heapify each list in the Hash Map.
        for diagonal in diagonals.values():
            heapq.heapify(diagonal)

        # Take values back out of the Hash Map.
        for row in range(m):
            for col in range(n):
                value = heapq.heappop(diagonals[row - col])
                mat[row][col] = value
        
        return mat
        
# @lc code=end

