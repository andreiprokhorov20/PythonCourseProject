"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/permutation-in-string/description
"""


class Solution:
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False
        cache1 = [0] * 26
        cache2 = [0] * 26
        for i in range(len(s1)):
            cache1[ord(s1[i]) - ord("a")] += 1
            cache2[ord(s2[i]) - ord("a")] += 1
        if cache1 == cache2:
            return True
        for i in range(len(s1), len(s2)):
            cache2[ord(s2[i - len(s1)]) - ord("a")] -= 1
            cache2[ord(s2[i]) - ord("a")] += 1
            if cache1 == cache2:
                return True
        return False
