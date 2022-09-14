#
# @lc app=leetcode id=1457 lang=python3
#
# [1457] Pseudo-Palindromic Paths in a Binary Tree
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
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        ans = 0
        def backtrack(root, curr):
            nonlocal ans
            if not root:
                return
            if not root.left and not root.right:
                curr[root.val - 1] += 1
                odds = sum([x % 2 for x in curr])
                curr[root.val - 1] -= 1 
                ans = ans + 1 if odds <= 1 else ans
                return
            curr[root.val - 1] += 1
            backtrack(root.left, curr)
            backtrack(root.right, curr)
            curr[root.val -1] -= 1
        backtrack(root, [0] * 9)
        return ans
        
# @lc code=end

