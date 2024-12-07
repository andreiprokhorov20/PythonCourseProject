"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/maximum-erasure-value/description
"""


class Solution(object):
    def maximumUniqueSubarray(self, nums):
        dict = {}
        i, j = 0, 0
        n = len(nums)
        maxsum = 0
        summ = 0
        while j < n:
            dict[nums[j]] = 1 if not nums[j] in dict else dict[nums[j]] + 1
            summ += nums[j]
            if dict[nums[j]] > 1:
                while dict[nums[j]] > 1:
                    dict[nums[i]] -= 1
                    summ -= nums[i]
                    i += 1
            maxsum = max(maxsum, summ)
            j += 1
        return maxsum
