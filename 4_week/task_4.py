"""
https://leetcode.com/problem-list/array/
url: https://leetcode.com/problems/group-anagrams/description
"""


class Solution:
    def groupAnagrams(self, strs):
        # ans = defaultdict(list)
        ans = []

        for s in strs:
            key = "".join(sorted(s))
            ans[key].append(s)

        return ans.values()
