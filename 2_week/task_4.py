"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/reverse-words-in-a-string/description
"""


class Solution:
    def reverseWords(self, s):
        arr = s.split()
        res = []
        for i in range(len(arr) - 1, -1, -1):
            res.append(arr[i])

        return " ".join(res)
