"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/integer-to-roman/description/
"""


class Solution(object):
    def intToRoman(self, num):
        ans = ""
        pair = [
            [1000, "M"],
            [900, "CM"],
            [500, "D"],
            [400, "CD"],
            [100, "C"],
            [90, "XC"],
            [50, "L"],
            [40, "XL"],
            [10, "X"],
            [9, "IX"],
            [5, "V"],
            [4, "IV"],
            [1, "I"],
        ]
        for i in range(len(pair)):
            while num >= pair[i][0]:
                ans += pair[i][1]
                num -= pair[i][0]
        return ans
