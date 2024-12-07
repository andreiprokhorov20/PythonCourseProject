"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/description
"""


class Solution:
    def maxSumTwoNoOverlap(self, nums, firstLen, secondLen):
        def getPrefix(number):
            maxsum = 0
            window = 0
            pntr = 0
            prefix = []
            while pntr < number:
                window += nums[pntr]
                if pntr == number - 1:
                    maxsum = max(maxsum, window)
                    prefix.append(window)
                else:
                    prefix.append(float("-inf"))
                pntr += 1
            while pntr < len(nums):
                window -= nums[pntr - number]
                window += nums[pntr]
                maxsum = max(maxsum, window)
                prefix.append(maxsum)
                pntr += 1
            return prefix

        def getPostfix(number):
            maxsum = 0
            window = 0
            pntr, count = len(nums) - 1, 0
            postfix = []
            while count < number:
                window += nums[pntr]
                if count == number - 1:
                    maxsum = max(maxsum, window)
                    postfix.append(window)
                else:
                    postfix.append(float("-inf"))
                count += 1
                pntr -= 1
            while pntr >= 0:
                window -= nums[pntr + number]
                window += nums[pntr]
                maxsum = max(maxsum, window)
                postfix.append(maxsum)
                pntr -= 1
            return postfix[::-1]

        prefixFirst, prefixSecond = getPrefix(firstLen), getPrefix(secondLen)
        postfixFirst, postfixSecond = getPostfix(firstLen), getPostfix(secondLen)
        print(prefixFirst, prefixSecond)
        maxsum = 0
        for i in range(len(prefixFirst) - 1):
            maxsum = max(maxsum, prefixFirst[i] + postfixSecond[i + 1])
        for i in range(len(prefixSecond) - 1):
            maxsum = max(maxsum, prefixSecond[i] + postfixFirst[i + 1])
        return maxsum
