"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/longest-turbulent-subarray/description
"""


class Solution(object):
    def maxTurbulenceSize(self, arr):
        length_arr = len(arr)
        res = 1
        curr_count = 1
        has_to_be_greater = 0
        for index in range(1, length_arr):
            if arr[index - 1] < arr[index] and (
                has_to_be_greater == 2 or has_to_be_greater == 0
            ):
                has_to_be_greater = 1
                curr_count += 1
            elif arr[index - 1] > arr[index] and (
                has_to_be_greater == 1 or has_to_be_greater == 0
            ):
                has_to_be_greater = 2
                curr_count += 1
            else:
                res = max(res, curr_count)
                if arr[index - 1] < arr[index]:
                    has_to_be_greater = 1
                    curr_count = 2
                elif arr[index - 1] > arr[index]:
                    has_to_be_greater = 2
                    curr_count = 2
                else:
                    has_to_be_greater = 0
                    curr_count = 1
            res = max(res, curr_count)
        return res
