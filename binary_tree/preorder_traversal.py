# https://leetcode.com/problems/binary-tree-preorder-traversal/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return res


class Solution2:
    def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        stack, node = [], root
        res = []
        while stack or node:
            while node:
                res.append(node.val)
                stack.append(node.right)
                node = node.left
            node = stack.pop()
        return res


def main():
    pass


if __name__ == '__main__':
    main()
