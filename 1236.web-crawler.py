#
# @lc app=leetcode id=1236 lang=python3
#
# [1236] Web Crawler
#
from lcimports import *
class HtmlParser(object):
   def getUrls(self, url):
       """
       :type url: str
       :rtype List[str]
       """

# @lc code=start
# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        visited = set()
        visited.add(startUrl)
        host = startUrl.split("://")[-1].split('/')[0]
        def dfs(node):
            urls = htmlParser.getUrls(node)
            for url in urls:
                if not url.startswith("http://" + host):
                    continue
                if url in visited:
                    continue
                visited.add(url)
                dfs(url)
        dfs(startUrl)
        return list(visited)
        
# @lc code=end

