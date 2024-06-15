# https://leetcode.com/problems/balanced-binary-tree/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_balanced = True

        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            left, right = dfs(node.left), dfs(node.right)
            if abs(left - right) > 1:
                nonlocal is_balanced
                is_balanced = False
            return max(left, right) + 1

        dfs(root)
        return is_balanced


class Solution2:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode]) -> tuple[int, bool]:
            if node is None:
                return 0, True
            (left, is_left_balanced), (right, is_right_balanced) = dfs(node.left), dfs(node.right)
            return max(left, right) + 1, is_left_balanced and is_right_balanced and abs(left - right) <= 1

        return dfs(root)[-1]


class SolutionReallyBalanced:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode]) -> tuple[int, int]:
            if node is None:
                return 0, 0
            left_min, left_max = dfs(node.left)
            right_min, right_max = dfs(node.right)
            curr_min = (min(left_min, right_min) if left_min and right_min else left_min or right_min) + 1
            curr_max = max(left_max, right_max) + 1
            return curr_min, curr_max

        min_level, max_level = dfs(root)
        print(min_level, max_level)
        return max_level - min_level <= 1


def main():
    pass


if __name__ == '__main__':
    main()
