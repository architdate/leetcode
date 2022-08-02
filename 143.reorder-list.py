#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
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
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def reverse(head):
            prev = None
            while head:
                temp = head.next
                head.next = prev
                prev = head
                head = temp
            return prev

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        rev = slow.next
        slow.next = None
        rev = reverse(rev)

        curr = head
        while rev:
            next = curr.next
            curr.next = rev
            rev = rev.next
            curr.next.next = next
            curr = next
        return head

        
# @lc code=end

