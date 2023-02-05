#
# @lc app=leetcode id=967 lang=python3
#
# [967] Numbers With Same Consecutive Differences
#
from lcimports import *
# @lc code=start
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        m = defaultdict(list)
        for i in range(10):
            if i + k <= 9:
                m[i].append(i + k)
            if i - k >= 0:
                m[i].append(i - k)
        ans = set()
        def dfs(n, curr):
            if n == 0:
                ans.add(int(curr))
                return
            for nei in m[int(curr[-1])]:
                dfs(n-1, curr + str(nei))
        for i in range(1, 10):
            dfs(n-1, str(i))
        return list(ans)
        
# @lc code=end

