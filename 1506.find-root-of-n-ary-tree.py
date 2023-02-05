#
# @lc app=leetcode id=1506 lang=python3
#
# [1506] Find Root of N-Ary Tree
#
from lcimports import *
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        children = set()
        vals = set()
        for n in tree:
            vals.add(n.val)
            for c in n.children:
                children.add(c)
        return list(vals - children)[0]
        
        
# @lc code=end

