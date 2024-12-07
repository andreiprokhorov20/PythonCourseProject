"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/swap-for-longest-repeated-character-substring/description
"""

from collections import Counter


class Solution:
    def maxRepOpt1(self, text):
        c = Counter(text)
        n = len(text)
        repeated = [1] * n
        for k in range(1, n):
            if text[k] == text[k - 1]:
                repeated[k] = repeated[k - 1] + 1
        i = n - 1
        maxx = 1
        while i > -1:
            currmax = repeated[i]
            prevrp = i - repeated[i] - 1
            if prevrp >= 0 and text[i] == text[prevrp]:
                currmax += repeated[i - currmax - 1]
            if c[text[i]] > currmax:
                currmax += 1
            maxx = max(maxx, currmax)
            i -= repeated[i]
        return maxx
