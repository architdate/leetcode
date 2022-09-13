#
# @lc app=leetcode id=637 lang=python3
#
# [637] Average of Levels in Binary Tree
#
from lcimports import *
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        q = [root]
        ans = []
        while q:
            lvl = []
            s, ct = 0, len(q)
            while q:
                n = q.pop(0)
                s += n.val
                if n.left:
                    lvl.append(n.left)
                if n.right:
                    lvl.append(n.right)
            if ct:
                ans.append(s / ct)
            q = lvl
        return ans
        
# @lc code=end

