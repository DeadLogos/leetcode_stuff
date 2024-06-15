# https://leetcode.com/problems/binary-tree-postorder-traversal/description/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        stack, node = [], root
        res = []
        while stack or node:
            while node:
                stack.append(node)
                node = node.left if node.left else node.right
            node = stack.pop()
            res.append(node.val)
            node = stack[-1].right if stack and stack[-1].left is node else None
        return res


def main():
    pass


if __name__ == '__main__':
    main()
