"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/word-break/description
"""


class Solution:
    def wordBreak(self, s, wordDict):
        dp = [True] + [False] * len(s)

        for i in range(1, len(s) + 1):
            for w in wordDict:
                start = i - len(w)
                if start >= 0 and dp[start] and s[start:i] == w:
                    dp[i] = True
                    break

        return dp[-1]
