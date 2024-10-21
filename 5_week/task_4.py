"""
https://leetcode.com/problem-list/hash-table
url: https://leetcode.com/problems/clone-graph/description
"""


class Solution:
    def cloneGraph(self, node):
        if not node:
            return None

        seen = {}

        def dfs(node):
            # copy = Node(node.val)
            copy = []
            seen[copy.val] = copy
            for i in node.neighbors:
                if i.val in seen:
                    copy.neighbors.append(seen[i.val])
                else:
                    copy.neighbors.append(dfs(i))
            return copy

        return dfs(node)
