"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/generate-parentheses/description/
"""


class Solution(object):
    def generateParenthesis(self, n):
        ans = []

        def pre_solution(s, open_count, close_count):
            if len(s) == 2 * n:
                ans.append("".join(s))
                return

            if open_count < n:
                s.append("(")
                pre_solution(s, open_count + 1, close_count)
                s.pop()

            if open_count > close_count:
                s.append(")")
                pre_solution(s, open_count, close_count + 1)
                s.pop()

        pre_solution([], 0, 0)
        return ans
