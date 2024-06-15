# https://leetcode.com/problems/minimum-depth-of-binary-tree

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        def dfs(node):
            if not node:
                return float('inf')
            if not node.left and not node.right:
                return 1
            return min(dfs(node.left), dfs(node.right)) + 1

        return dfs(root)


class Solution2:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            left, right = dfs(node.left), dfs(node.right)
            return (min(left, right) if left and right else left or right) + 1

        return dfs(root)


def main():
    pass


if __name__ == '__main__':
    main()
