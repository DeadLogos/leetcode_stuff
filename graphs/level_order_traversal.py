# https://leetcode.com/problems/binary-tree-level-order-traversal/

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def level_order(self, root: Optional[TreeNode]) -> list[list[int]]:
        if root is None:
            return []
        res = []
        deq = deque([root])
        while deq:
            size = len(deq)
            res.append([])
            for _ in range(size):
                node = deq.popleft()
                res[-1].append(node.val)
                if node.left:
                    deq.append(node.left)
                if node.right:
                    deq.append(node.right)
        return res

    def level_order_dfs(self, root: Optional[TreeNode]):
        res = []

        def dfs(node, level=0):
            if node:
                if level == len(res):
                    res.append([])
                res[level].append(node.val)
                dfs(node.left, level + 1)
                dfs(node.right, level + 1)
        dfs(root)
        return res


def main():
    pass


if __name__ == '__main__':
    main()
