"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/palindrome-partitioning/description/
"""

class Solution(object):
    def partition(self, s):
        result = []

        def palindrome(s):
            return s == s[::-1]
        
        def dfs(s, j, path, result):
            if j == len(s):
                result.append(path)
                return
            for i in range(j, len(s)):
                if palindrome(s[j: i + 1]):
                    dfs(s, i + 1, path + [s[j: i + 1]], result)
            
        dfs(s, 0, [], result)
        return result
