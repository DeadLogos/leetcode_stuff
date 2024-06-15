# https://leetcode.com/problems/validate-binary-search-tree/description/

from math import inf
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node: Optional[TreeNode], low=-inf, high=inf):
            if node is None:
                return True
            return low < node.val < high and helper(node.left, low, node.val) and helper(node.right, node.val, high)

        return helper(root)


def main():
    pass


if __name__ == '__main__':
    main()
