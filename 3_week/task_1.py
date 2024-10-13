"""
https://leetcode.com/problem-list/array/
url: https://leetcode.com/problems/container-with-most-water/description
"""


class Solution(object):
    def maxArea(self, height):
        p1 = 0
        p2 = len(height) - 1
        ans = 0
        while p1 != p2:
            h = min(height[p1], height[p2])
            if ((p2 - p1) * h) > ans:
                ans = (p2 - p1) * h
            if height[p1] < height[p2]:
                p1 += 1
            else:
                p2 += 1
        return ans
