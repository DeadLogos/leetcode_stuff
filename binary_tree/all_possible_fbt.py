# https://leetcode.com/problems/all-possible-full-binary-trees/description/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def allPossibleFBT(self, n: int) -> list[Optional[TreeNode]]:
        if not n % 2:
            return []
        if n == 1:
            return [TreeNode()]
        res = []
        for i in range(1, n, 2):
            left_trees, right_trees = self.allPossibleFBT(n - i - 1), self.allPossibleFBT(i)
            for left in left_trees:
                for right in right_trees:
                    res.append(TreeNode(left=left, right=right))
        return res


def main():
    pass


if __name__ == '__main__':
    main()
