#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#

# @lc code=start
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if curr.children[idx] == None:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if curr.children[idx] == None:
                return False
            curr = curr.children[idx]
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            idx = ord(c) - ord('a')
            if curr.children[idx] == None:
                return False
            curr = curr.children[idx]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

