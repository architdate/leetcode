#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        def dfs(s, p):
            if s == "":
                if len(p) % 2 != 0:
                    return False
                for i, c in enumerate(p):
                    if i % 2 != 0 and c != '*':
                        return False
                return True 
            if len(p) == 0:
                return False
            if (s, p) in memo:
                return memo[(s, p)]
            ans = False
            if len(p) >= 2 and p[1] == '*':
                ans = ans or dfs(s, p[2:])
            if p.startswith('.*') or p.startswith(s[0] + '*'):
                ans = ans or dfs(s[1:], p) or dfs(s[1:], p[2:])
            elif p[0] == '.' or p[0] == s[0]:
                ans = ans or dfs(s[1:], p[1:])
            memo[(s, p)] = ans
            return ans
        return dfs(s, p)
        
# @lc code=end

