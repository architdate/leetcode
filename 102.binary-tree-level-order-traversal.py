#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = [[root.val]]
        q = [root]
        while q:
            next_level = []
            level = []
            while q:
                n = q.pop(0)
                if n.left:
                    next_level.append(n.left)
                    level.append(n.left.val)
                if n.right:
                    next_level.append(n.right)
                    level.append(n.right.val)
            if next_level:
                q = next_level
                ans.append(level)
        return ans

        
# @lc code=end

