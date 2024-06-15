# https://leetcode.com/problems/find-largest-value-in-each-tree-row/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> list[int]:
        res = []

        def dfs(node, level=0):
            if node is None:
                return
            if len(res) == level:
                res.append(node.val)
            res[level] = max(res[level], node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root)
        return res


def main():
    pass


if __name__ == '__main__':
    main()
