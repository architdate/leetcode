#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#
from lcimports import *
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        node_map = {}
        def dfs(node):
            if node in node_map:
                return node_map[node]
            new_node = Node(node.val)
            node_map[node] = new_node
            for n in node.neighbors:
                new_node.neighbors.append(dfs(n))
            return new_node
        clone = dfs(node)
        return clone
        
# @lc code=end

