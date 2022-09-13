#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#
from lcimports import *
# @lc code=start
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s = []
        while head:
            s.append(head.val)
            head = head.next
        return s == s[::-1]
        
# @lc code=end

