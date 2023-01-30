#
# @lc app=leetcode id=1888 lang=python3
#
# [1888] Minimum Number of Flips to Make the Binary String Alternating
#

# @lc code=start
class Solution:
    def minFlips(self, s: str) -> int:
        minimumFlips = len(s)
        
        # Window Size
        k = len(s)
        
        # For strings of odd length, double them
        # So that we do not have to manually perform type-1 operation 
        # that is, taking each bit and moving to end of string
        s = s if k % 2 == 0 else s + s
        
        # There can be only two valid alternating strings as we only have 0 and 1
        # One starts with 0 and other with 1
        # e.g. for a string of length 3 we can have either 010 or 101
        altArr1, altArr2 = [], []        
        for i in range(len(s)):
            altArr1.append("0" if i % 2 == 0 else "1")
            altArr2.append("1" if i % 2 == 0 else "0")
            
        alt1 = "".join(altArr1)
        alt2 = "".join(altArr2)
        
        
        # Minimum Number of operations = Minimum Difference between the string and alt2 and alt3
        diff1, diff2 = 0,0
        
        # Sliding Window Template Begins
        i,j = 0,0
        
        
        while j < len(s):
            if s[j] != alt1[j] : diff1 += 1
            if s[j] != alt2[j] : diff2 += 1
                
            if j - i + 1 < k: j += 1
            else:
                minimumFlips = min(minimumFlips, diff1, diff2)
                if s[i] != alt1[i] : diff1 -= 1
                if s[i] != alt2[i] : diff2 -= 1
                i += 1
                j += 1
        
        return minimumFlips
        
# @lc code=end

