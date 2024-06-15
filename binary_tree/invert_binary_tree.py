# https://leetcode.com/problems/invert-binary-tree/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# O(n) memory
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        def helper(node, curr):
            if node.left:
                curr.right = TreeNode(node.left.val)
                helper(node.left, curr.right)
            if node.right:
                curr.left = TreeNode(node.right.val)
                helper(node.right, curr.left)

        res = TreeNode(root.val)
        helper(root, res)
        return res


# in-place
class Solution2:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(node):
            if node is None:
                return
            node.right, node.left = node.left, node.right
            helper(node.left)
            helper(node.right)

        helper(root)
        return root


# in-place iterative pre-order traversal
class Solution3:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.right, node.left = node.left, node.right
                stack.append(node.right)
                stack.append(node.left)
        return root


def main():
    pass


if __name__ == '__main__':
    main()
