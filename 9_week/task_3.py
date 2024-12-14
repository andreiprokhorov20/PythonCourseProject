"""
https://leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/unique-binary-search-trees-ii/description
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def generateTrees(self, n):
        if n == 0:
            return []
        memo = {}

        def generate_trees(start, end):
            if (start, end) in memo:
                return memo[(start, end)]
            trees = []
            if start > end:
                trees.append(None)
                return trees
            for root_val in range(start, end + 1):
                left_trees = generate_trees(start, root_val - 1)
                right_trees = generate_trees(root_val + 1, end)
                for left_tree in left_trees:
                    for right_tree in right_trees:
                        root = TreeNode(root_val, left_tree, right_tree)
                        trees.append(root)
            memo[(start, end)] = trees
            return trees

        return generate_trees(1, n)
