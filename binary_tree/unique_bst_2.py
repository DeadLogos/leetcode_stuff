# https://leetcode.com/problems/unique-binary-search-trees-ii/description/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> list[Optional[TreeNode]]:
        def helper(l, r):
            if l > r:
                return [None]
            res = []
            for i in range(l, r + 1):
                left_subtrees, right_subtrees = helper(l, i - 1), helper(i + 1, r)
                for lt in left_subtrees:
                    for rt in right_subtrees:
                        res.append(TreeNode(val=i, left=lt, right=rt))
            return res

        return helper(1, n)


def main():
    pass


if __name__ == '__main__':
    main()
