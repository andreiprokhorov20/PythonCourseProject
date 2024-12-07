"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/binary-subarrays-with-sum/description
"""


class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        count = 0
        summ = 0
        dictionary = {0: 1}
        for i in nums:
            summ += i
            complement = summ - goal
            if complement in dictionary:
                count += dictionary[complement]
            dictionary[summ] = dictionary.get(summ, 0) + 1
        return count
