"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/minimum-size-subarray-sum/description
"""


class Solution(object):
    def minSubArrayLen(self, target, nums):
        left = 0
        right = 0
        min_size = float("inf")
        sum = nums[0]
        if nums[0] >= target:
            return 1
        while right + 1 < len(nums):
            while sum < target and (right + 1 < len(nums)):
                right += 1
                sum += nums[right]
            if sum >= target:
                min_size = min(min_size, right - left + 1)
            while sum >= target and left < right:
                if sum >= target:
                    min_size = min(min_size, right - left + 1)
                sum -= nums[left]
                left += 1
            if sum >= target:
                min_size = min(min_size, right - left + 1)
            if min_size == 1:
                return 1
        if min_size == float("inf"):
            return 0
        else:
            return min_size
