#
# @lc app=leetcode id=1189 lang=python3
#
# [1189] Maximum Number of Balloons
#
from lcimports import *
# @lc code=start
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq = Counter(text)
        return min(freq['b'], freq['a'], freq['l'] // 2, freq['o'] // 2, freq['n'])
        
# @lc code=end

