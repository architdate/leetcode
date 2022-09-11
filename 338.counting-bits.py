#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#
from lcimports import *
# @lc code=start
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]
        while len(ans) <= n:
            ans += [i+1 for i in ans]
        return ans[:n+1]
        
# @lc code=end

