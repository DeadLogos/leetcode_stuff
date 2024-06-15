# https://leetcode.com/problems/symmetric-tree/description/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def dfs(node1: Optional[TreeNode], node2: Optional[TreeNode]):
            if node1 and node2:
                if node1.val != node2.val:
                    return False
                return dfs(node1.left, node2.right) and dfs(node1.right, node2.left)
            return node1 is None and node2 is None

        return dfs(root.left, root.right)


class Solution2:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(node1, node2):
            if node1 and node2:
                return node1.val == node2.val and dfs(node1.left, node2.right) and dfs(node1.right, node2.left)
            return node1 is None and node2 is None
        return dfs(root, root)


def main():
    pass


if __name__ == '__main__':
    main()
