# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def helper(node, left_path=0, right_path=0):
            if not node.left:
                self.res = max(self.res, left_path)
            else:
                helper(node.left, 0, left_path + 1)
            if not node.right:
                self.res = max(self.res, right_path)
            else:
                helper(node.right, right_path + 1, 0)

        helper(root)
        return self.res


class Solution2:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def helper(node, was_right=True, path=0):
            if not node:
                self.res = max(self.res, path - 1)
            elif was_right:
                helper(node.left, False, path + 1)
                helper(node.right, True, 1)
            else:
                helper(node.left, False, 1)
                helper(node.right, True, path + 1)

        helper(root, True, 0)
        return self.res


class Solution3:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def helper(node, was_right=True, path=0):
            if not node:
                return path - 1
            if was_right:
                return max(helper(node.left, False, path + 1), helper(node.right, True, 1))
            else:
                return max(helper(node.left, False, 1), helper(node.right, True, path + 1))

        return helper(root)


def main():
    pass


if __name__ == '__main__':
    main()
