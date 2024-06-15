# https://leetcode.com/problems/diameter-of-binary-tree/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]

        def helper(node):
            if node is None:
                return 0
            left_max, right_max = helper(node.left), helper(node.right)
            res[0] = max(res[0], left_max + right_max + 1)
            return max(left_max, right_max) + 1

        helper(root)
        return res[0] - 1


class Solution2:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            if node is None:
                return 0, 0
            (left_depth, left_diam), (right_depth, right_diam) = helper(node.left), helper(node.right)
            return max(left_depth, right_depth) + 1, max(left_diam, right_diam, left_depth + right_depth + 1)

        return helper(root)[-1] - 1


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.left.left = TreeNode(6)
    root.left.right.left = TreeNode(8)
    root.left.right.left.right = TreeNode(10)
    print(Solution().diameterOfBinaryTree(root))


if __name__ == '__main__':
    main()
