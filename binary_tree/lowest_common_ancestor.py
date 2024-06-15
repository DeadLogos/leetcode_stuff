# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.res = None

        def dfs(node):
            if node is None:
                return False, False
            left, right = dfs(node.left), dfs(node.right)
            if all(left):
                self.res = node.left
                return False, False
            if all(right):
                self.res = node.right
                return False, False
            return node == p or left[0] or right[0], node == q or left[1] or right[1]

        dfs(root)

        return self.res or root


def main():
    pass


if __name__ == '__main__':
    main()
