#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#
from lcimports import *
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return
        prev = base = ListNode(0, next=head)
        curr = head
        while curr:
            while curr and curr.val == val:
                curr = curr.next
                prev.next = curr
            if not curr:
                break
            prev, curr = curr, curr.next
        return base.next

        
# @lc code=end

