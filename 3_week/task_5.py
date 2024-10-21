"""
https://leetcode.com/problem-list/array/
url: https://leetcode.com/problems/combination-sum/description
"""


class Solution:
    def combinationSum(self, candidates, target):
        res = []

        def make_combination(idx, comb, total):
            if total == target:
                res.append(comb[:])
                return
            if total > target or idx >= len(candidates):
                return
            comb.append(candidates[idx])
            make_combination(idx, comb, total + candidates[idx])
            comb.pop()
            make_combination(idx + 1, comb, total)
            return res

        return make_combination(0, [], 0)
