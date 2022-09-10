#
# @lc app=leetcode id=261 lang=python3
#
# [261] Graph Valid Tree
#
from lcimports import *
# @lc code=start
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i:[] for i in range(n)}
        for e1, e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)
        
        def dfs(node, parent):
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                if neighbor in visited:
                    return False
                if not dfs(neighbor, node):
                    return False
            return True

        visited = set()
        if not dfs(0, None):
            return False
        return len(visited) == n
        
# @lc code=end

