# https://leetcode.com/problems/count-complete-tree-nodes/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return 0
            return dfs(node.left) + dfs(node.right) + 1

        return dfs(root)


def main():
    pass


if __name__ == '__main__':
    main()
