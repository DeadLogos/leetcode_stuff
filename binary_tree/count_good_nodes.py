# https://leetcode.com/problems/count-good-nodes-in-binary-tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(node, mx):
            if node is None:
                return 0
            mx = max(mx, node.val)
            return helper(node.left, mx) + helper(node.right, mx) + (mx == node.val)
        return helper(root, float('-inf'))


def main():
    pass


if __name__ == '__main__':
    main()
