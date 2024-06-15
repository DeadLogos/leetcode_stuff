# https://leetcode.com/problems/binary-tree-maximum-path-sum/


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            if node is None:
                return float('-inf'), 0

            l_max_path, l_max_side = helper(node.left)
            r_max_path, r_max_side = helper(node.right)

            curr_max_path = max(l_max_path, r_max_path, l_max_side + r_max_side + node.val)
            curr_max_side = max(node.val + max(l_max_side, r_max_side), 0)
            return curr_max_path, curr_max_side
        return helper(root)[0]


def main():
    path


if __name__ == '__main__':
    main()
