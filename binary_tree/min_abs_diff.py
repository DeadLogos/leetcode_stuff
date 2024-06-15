# https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/

from typing import Optional
from is_balanced import TreeNode


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        res = [float('-inf'), float('inf')]  # 0 - previous value  1 - current min difference
        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            res[1] = min(res[1], node.val - res[0])
            res[0] = node.val
            dfs(node.right)

        dfs(root)
        return res[1] if res[1] != float('inf') else -1


def main():
    pass


if __name__ == '__main__':
    main()
