#
# @lc app=leetcode id=271 lang=python3
#
# [271] Encode and Decode Strings
#
from typing import *
# @lc code=start
class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        if not strs:
            return chr(999)
        return chr(998).join(strs)
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        if s == chr(999):
            return []
        return s.split(chr(998))


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
# @lc code=end

