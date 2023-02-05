#
# @lc app=leetcode id=1614 lang=python3
#
# [1614] Maximum Nesting Depth of the Parentheses
#

# @lc code=start
class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        st = []
        for c in s:
            if c != '(' and c != ')':
                continue
            if c == '(':
                st.append(c)
                ans = max(ans, len(st))
            else:
                st.pop()
        return ans
        
# @lc code=end

