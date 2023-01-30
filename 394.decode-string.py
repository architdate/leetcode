#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        parity_map = {}
        st = []
        for i, c in enumerate(s):
            if c == "[":
                st.append(i)
            if c == "]":
                parity_map[st.pop()] = i
        def helper(l, r):
            ans = ""
            num = 0
            i = l
            while i <= r:
                if s[i].isdigit():
                    num = (num * 10) + int(s[i])
                    i += 1
                elif s[i] == "[":
                    ans += (num * helper(i+1, parity_map[i]-1))
                    num = 0
                    i = parity_map[i] + 1
                else:
                    ans += s[i]
                    i += 1
            return ans
        return helper(0, len(s)-1)
        
# @lc code=end

