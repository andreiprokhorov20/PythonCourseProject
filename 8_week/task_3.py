"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/frequency-of-the-most-frequent-element/description
"""


class Solution:
    def maxFrequency(self, nums, k):
        n = len(nums)
        nums.sort()
        preSum = [0] * (n + 1)
        for i in range(n):
            preSum[i + 1] = preSum[i] + nums[i]

        def getSum(left, right):
            return preSum[right + 1] - preSum[left]

        def count(index):
            left = 0
            right = index
            res = index
            while left <= right:
                mid = left + (right - left) // 2
                s = getSum(mid, index - 1)
                if s + k >= (index - mid) * nums[index]:
                    res = mid
                    right = mid - 1
                else:
                    left = mid + 1
            return index - res + 1

        ans = 0
        for i in range(n):
            ans = max(ans, count(i))
        return ans
