"""
https://leetcode.com/problem-list/array/
url: https://leetcode.com/problems/combination-sum-ii/description
"""


class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []

        def dfs(target, start, comb):
            if target < 0:
                return
            if target == 0:
                res.append(comb)
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > target:
                    break
                dfs(target - candidates[i], i + 1, comb + [candidates[i]])

        dfs(target, 0, [])
        return res
