# https://leetcode.com/problems/recover-binary-search-tree/


from math import inf
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @classmethod
    def dfs(cls, root: TreeNode, res=None):
        if res is None:
            res = []
        if root is None:
            return
        cls.dfs(root.left, res)
        res.append(root)
        cls.dfs(root.right, res)
        return res

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        nodes = self.dfs(root, [TreeNode(-inf)])
        nodes.append(TreeNode(inf))
        a = b = None
        for i in range(1, len(nodes) - 1):
            if nodes[i].val > nodes[i + 1].val > nodes[i - 1].val:
                a = nodes[i]
            if nodes[i].val < nodes[i - 1].val < nodes[i + 1].val:
                b = nodes[i]
            if a and b:
                break
        a.val, b.val = b.val, a.val


def main():
    pass


if __name__ == '__main__':
    main()
