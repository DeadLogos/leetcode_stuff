# https://leetcode.com/problems/maximum-depth-of-binary-tree/


from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def max_depth_bfs(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        deq = deque([root])
        level = 0
        while deq:
            level += 1
            for _ in range(len(deq)):
                node = deq.popleft()
                if node.left:
                    deq.append(node.left)
                if node.right:
                    deq.append(node.right)
        return level

    def max_depth_dfs(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return max(self.max_depth_dfs(root.left), self.max_depth_dfs(root.right)) + 1


def main():
    pass


if __name__ == '__main__':
    main()
