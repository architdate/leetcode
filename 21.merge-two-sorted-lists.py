#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#
from typing import *
from lcimports import *
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=list2)
        prev, curr = dummy, list2
        while curr:
            if not list1:
                break
            if curr.val <= list1.val:
                prev = curr
                curr = curr.next
            else:
                prev.next = list1
                list1 = list1.next
                prev.next.next = curr
                prev = prev.next
        if list1:
            prev.next = list1
        return dummy.next
        
# @lc code=end

