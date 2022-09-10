#
# @lc app=leetcode id=323 lang=python3
#
# [323] Number of Connected Components in an Undirected Graph
#
from lcimports import *
# @lc code=start
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}
        for e1, e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)

        def dfs(node):
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        
        visited = set()
        connected_components = 0
        for i in range(n):
            if i in visited:
                continue
            connected_components += 1
            dfs(i)
        return connected_components
        
# @lc code=end

