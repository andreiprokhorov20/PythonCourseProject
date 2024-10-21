"""
https://leetcode.com/problem-list/array/
url: https://leetcode.com/problems/next-permutation/description
"""


class Solution:
    def nextPermutation(self, nums):
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[j], nums[i] = nums[i], nums[j]
        nums[i + 1 :] = reversed(nums[i + 1 :])
