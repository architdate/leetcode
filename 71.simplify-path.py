#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        # "/home/../foo/" -> "/foo"
        # "/home/./foo" -> "/home/foo"
        path = path.split("/")
        path = [p for p in path if p != "" and p != "."]
        stk = []
        for i, p in enumerate(path):
            if p == "..":
                if not stk:
                    continue
                stk.pop()
            else:
                stk.append(p)
        return '/'+'/'.join(stk)
        
# @lc code=end

