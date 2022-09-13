#
# @lc app=leetcode id=393 lang=python3
#
# [393] UTF-8 Validation
#
from lcimports import *
# @lc code=start
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        byte_ct = 0
        mask1 = 1 << 7
        mask2 = 1 << 6
        for num in data:
            if byte_ct == 0:
                mask = 1 << 7
                while mask & num:
                    byte_ct += 1
                    mask >>= 1
                if byte_ct == 0:
                    continue
                if byte_ct == 1 or byte_ct > 4:
                    return False
            else:
                if mask1 & num == 0 or mask2 & num:
                    return False
            byte_ct -= 1
        return byte_ct == 0

        
# @lc code=end

