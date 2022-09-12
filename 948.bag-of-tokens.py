#
# @lc app=leetcode id=948 lang=python3
#
# [948] Bag of Tokens
#
from lcimports import *
# @lc code=start
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        curr = 0
        ans = 0
        l, r = 0, len(tokens)-1
        while l <= r:
            if power >= tokens[l]:
                power -= tokens[l]
                l += 1
                curr += 1
                ans = max(ans, curr)
            else:
                if curr == 0:
                    break
                power += tokens[r]
                r -= 1
                curr -= 1
        return ans
            
        
# @lc code=end

