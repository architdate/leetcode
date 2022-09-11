#
# @lc app=leetcode id=763 lang=python3
#
# [763] Partition Labels
#
from lcimports import *
# @lc code=start
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans = []
        last = {c: i for i, c in enumerate(s)}
        processed = -1
        currmax = 0
        for i, c in enumerate(s):
            currmax = max(currmax, last[c])
            if i == currmax:
                ans.append(currmax - processed)
                processed += ans[-1]
        return ans
        
# @lc code=end

