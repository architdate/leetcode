#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = [root.val]
        q = [root]
        while q:
            next_level = []
            while q:
                n = q.pop(0)
                if n.left:
                    next_level.append(n.left)
                if n.right:
                    next_level.append(n.right)
            if next_level:
                q = next_level
                ans.append(next_level[-1].val)
        return ans
        
# @lc code=end

