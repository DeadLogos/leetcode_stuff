# https://leetcode.com/problems/path-sum-iii/

from typing import Optional
from collections import Counter


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], target: int) -> int:
        prefix = Counter([0])

        def dfs(node, curr=0):
            if node is None:
                return 0
            curr += node.val
            res = prefix[curr - target]
            prefix[curr] += 1
            res += dfs(node.left, curr) + dfs(node.right, curr)
            prefix[curr] -= 1
            return res

        return dfs(root)


def main():
    pass


if __name__ == '__main__':
    main()
