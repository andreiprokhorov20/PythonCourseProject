"""
https://leetcode.com/problem-list/array/
url: https://leetcode.com/problems/maximum-subarray/description
"""


class Solution:
    def maxSubArray(self, nums):
        res = nums[0]
        total = 0

        for n in nums:
            if total < 0:
                total = 0

            total += n
            res = max(res, total)

        return res
