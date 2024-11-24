"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/maximum-length-of-repeated-subarray/description
"""


class Solution:
    def findLength(self, nums1, nums2):
        strnum2 = "".join([chr(x) for x in nums2])
        strmax = ""
        ans = 0
        for num in nums1:
            strmax += chr(num)
            if strmax in strnum2:
                ans = max(ans, len(strmax))
            else:
                strmax = strmax[1:]
        return ans
