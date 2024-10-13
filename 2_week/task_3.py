"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/decode-ways/description
"""


class Solution(object):
    def numDecodings(self, s):
        if s[0] == "0":
            return 0
        d = [1, 1] + (
            [
                0,
            ]
            * (len(s) - 1)
        )
        for i in range(1, len(s)):
            if (int(s[i]) >= 1) and (int(s[i]) <= 9):
                d[i + 1] += d[i]
            if (int(s[i - 1] + s[i]) >= 10) and (int(s[i - 1] + s[i]) <= 26):
                d[i + 1] += d[i - 1]
        return d[-1]
