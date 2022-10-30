#
# @lc app=leetcode id=929 lang=python3
#
# [929] Unique Email Addresses
#
from lcimports import *
# @lc code=start
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        for e in emails:
            local, domain = e.split('@')
            local = local.replace('.', '').split('+')[0]
            unique.add(local + '@' + domain)
        return len(unique)
        
# @lc code=end

