"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/arithmetic-slices/description
"""


class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        ans = 0
        if len(nums) < 3:
            return 0
        p1 = 0
        p2 = 2
        while p1 < len(nums) - 1 and p2 <= len(nums) - 1:
            lenght_subarr = 0
            if nums[p1 + 1] - nums[p1] == nums[p1 + 2] - nums[p1 + 1]:
                lenght_subarr += 1
                if p2 < len(nums) - 1:
                    p2 += 1
                    while nums[p2 - 1] - nums[p2 - 2] == nums[p2] - nums[p2 - 1]:
                        lenght_subarr += 1
                        if p2 < len(nums) - 1:
                            p2 += 1
                        else:
                            break
            ans += lenght_subarr * (lenght_subarr - 1) / 2 + lenght_subarr
            p1 = p2 - 1
            p2 += 1
        return ans
