# https://leetcode.com/problems/binary-tree-right-side-view/


from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        if root is None:
            return []
        res = []
        deq = deque([root])
        while deq:
            res.append(deq[-1].val)
            for _ in range(len(deq)):
                node = deq.popleft()
                if node.left:
                    deq.append(node.left)
                if node.right:
                    deq.append(node.right)
        return res


def main():
    pass


if __name__ == '__main__':
    main()
