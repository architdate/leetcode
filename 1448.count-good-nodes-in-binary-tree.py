#
# @lc app=leetcode id=1448 lang=python3
#
# [1448] Count Good Nodes in Binary Tree
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
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def backtrack(n, path_largest):
            nonlocal count
            if not n:
                return
            if n.val >= path_largest:
                count += 1
            backtrack(n.left, max(path_largest, n.val))
            backtrack(n.right, max(path_largest, n.val))
        backtrack(root, -inf)
        return count
        
# @lc code=end

