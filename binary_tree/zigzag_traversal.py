# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'Node[{self.val}]'


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        deq, is_even_level = deque([root]), True
        res = []
        while deq:
            level_arr = []
            for _ in range(len(deq)):
                if is_even_level:
                    node = deq.popleft()
                    if node:
                        level_arr.append(node.val)
                        deq.append(node.left)
                        deq.append(node.right)
                else:
                    node = deq.pop()
                    if node:
                        level_arr.append(node.val)
                        deq.appendleft(node.right)
                        deq.appendleft(node.left)
            is_even_level = not is_even_level
            if level_arr:
                res.append(level_arr)
        return res


def main():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    root.left.right = TreeNode(4)
    print(Solution().zigzagLevelOrder(root))


if __name__ == '__main__':
    main()
