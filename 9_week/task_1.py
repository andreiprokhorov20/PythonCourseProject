"""
https://leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/validate-binary-search-tree/description
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def isValidBST(self, root):
        def add_func(node, mini, maxi):
            if not node:
                return True
            if node.val <= mini or node.val >= maxi:
                return False
            return add_func(node.left, mini, node.val) and add_func(
                node.right, node.val, maxi
            )

        return add_func(root, float("-inf"), float("inf"))
