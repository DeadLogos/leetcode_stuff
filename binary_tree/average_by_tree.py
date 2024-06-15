# https://leetcode.com/problems/average-of-levels-in-binary-tree/

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> list[float]:
        deq = deque([root])
        res = []
        while deq:
            total, summ = len(deq), 0
            for _ in range(total):
                node = deq.popleft()
                summ += node.val
                if node.left:
                    deq.append(node.left)
                if node.right:
                    deq.append(node.right)
            res.append(round(summ / total, 5))
        return res


def main():
    pass


if __name__ == '__main__':
    main()
