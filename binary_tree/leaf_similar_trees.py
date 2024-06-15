# https://leetcode.com/problems/leaf-similar-trees/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def helper(node):
            if not node.left and not node.right:
                yield node.val
            if node.left:
                yield from helper(node.left)
            if node.right:
                yield from helper(node.right)

        return list(helper(root1)) == list(helper(root2))


class Solution2:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def helper(node):
            if not node.left and not node.right:
                yield node.val
            if node.left:
                yield from helper(node.left)
            if node.right:
                yield from helper(node.right)

        g1, g2 = helper(root1), helper(root2)
        for x1 in g1:
            try:
                x2 = next(g2)
            except StopIteration:
                return False
            if x1 != x2:
                return False
        try:
            next(g2)
        except StopIteration:
            return True
        else:
            return False


def main():
    pass


if __name__ == '__main__':
    main()
