#
# @lc app=leetcode id=1823 lang=python3
#
# [1823] Find the Winner of the Circular Game
#

# @lc code=start
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def helper(n, k):
            if n == 1:
                return 0
            return (helper(n-1, k) + k) % n
        return helper(n, k) + 1
        
# @lc code=end

