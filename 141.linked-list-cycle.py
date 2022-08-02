#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#
from typing import *
from lcimports import *
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = set()
        while head:
            if head in s:
                return True
            s.add(head)
            head = head.next
        return False
        
# @lc code=end

