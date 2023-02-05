#
# @lc app=leetcode id=845 lang=python3
#
# [845] Longest Mountain in Array
#
from lcimports import *
# @lc code=start
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        N = len(arr)
        ans = base = 0

        while base < N:
            end = base
            if end + 1 < N and arr[end] < arr[end + 1]: #if base is a left-boundary
                #set end to the peak of this potential mountain
                while end+1 < N and arr[end] < arr[end+1]:
                    end += 1

                if end + 1 < N and arr[end] > arr[end + 1]: #if end is really a peak..
                    #set 'end' to right-boundary of mountain
                    while end+1 < N and arr[end] > arr[end+1]:
                        end += 1
                    #record candidate answer
                    ans = max(ans, end - base + 1)

            base = max(end, base + 1)

        return ans
        
# @lc code=end

