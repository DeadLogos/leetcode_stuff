# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# recursion
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        self.curr = TreeNode()

        def dfs(node):
            if node is None:
                return
            left, right = node.left, node.right
            node.left = node.right = None
            self.curr.right = node
            self.curr = self.curr.right
            dfs(left)
            dfs(right)

        dfs(root)
        return root


class Solution2:
    def flatten(self, root: Optional[TreeNode]) -> None:
        def dfs(node) -> Optional[TreeNode]:
            if node is None:
                return
            left_tail = dfs(node.left)
            right_tail = dfs(node.right)
            if left_tail:
                node.right, left_tail.right, node.left = node.left, node.right, None
            return right_tail or left_tail or node

        dfs(root)


# optimal approach
class Solution3:
    def flatten(self, root: Optional[TreeNode]) -> None:
        node = root
        while node:
            if node.left:
                tail = node.left
                while tail.right:
                    tail = tail.right
                node.right, node.left, tail.right = node.left, None, node.right
            node = node.right


def main():
    pass


if __name__ == '__main__':
    main()
