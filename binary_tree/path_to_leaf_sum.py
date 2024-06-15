# https://leetcode.com/problems/path-sum/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        def helper(node, curr_sum=0):
            if node is None:
                return False
            if node.left is None and node.right is None:
                return curr_sum + node.val == targetSum
            return helper(node.left, curr_sum + node.val) or helper(node.right, curr_sum + node.val)

        return helper(root)


def main():
    pass


if __name__ == '__main__':
    main()
