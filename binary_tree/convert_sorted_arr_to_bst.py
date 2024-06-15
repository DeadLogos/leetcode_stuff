# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        def dfs(l, r):
            if l > r:
                return None
            middle = (l + r) // 2
            node = TreeNode(nums[middle])
            node.left = dfs(l, middle - 1)
            node.right = dfs(middle + 1, r)
            return node

        return dfs(0, len(nums) - 1)


def main():
    pass


if __name__ == '__main__':
    main()
