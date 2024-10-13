"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/zigzag-conversion/description/
"""


class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
        rows = [[] for i in range(numRows)]
        index = 0
        step = 1
        for char in s:
            rows[index].append(char)
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step
        for i in range(numRows):
            rows[i] = "".join(rows[i])
        return "".join(rows)
