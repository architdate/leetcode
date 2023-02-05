#
# @lc app=leetcode id=1472 lang=python3
#
# [1472] Design Browser History
#
from lcimports import *
# @lc code=start
class Node:
    def __init__(self, page, prev = None, next = None):
        self.page = page
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = Node(homepage)

    def visit(self, url: str) -> None:
        self.curr.next = Node(url, prev=self.curr)
        self.curr = self.curr.next

    def back(self, steps: int) -> str:
        while steps > 0 and self.curr.prev != None:
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.page

    def forward(self, steps: int) -> str:
        while steps > 0 and self.curr.next != None:
            self.curr = self.curr.next
            steps -= 1
        return self.curr.page
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
# @lc code=end

