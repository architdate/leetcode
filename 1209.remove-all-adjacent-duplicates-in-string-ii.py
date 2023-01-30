#
# @lc app=leetcode id=1209 lang=python3
#
# [1209] Remove All Adjacent Duplicates in String II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        st = []
        for c in s:
            if st and st[-1][0] == c:
                if st[-1][1] == k - 1:
                    st.pop()
                else:
                    st[-1][1] += 1
            else:
                st.append([c, 1])
        ans = ""
        for c, v in st:
            ans += c * v
        return ans
        
# @lc code=end

