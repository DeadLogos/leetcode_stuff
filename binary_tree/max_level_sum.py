# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description/

from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        deq = deque([root])
        level, res_level, max_sum = 0, 0, float('-inf')
        while deq:
            level += 1
            curr_sum = 0
            for _ in range(len(deq)):
                node = deq.popleft()
                curr_sum += node.val
                if node.left:
                    deq.append(node.left)
                if node.right:
                    deq.append(node.right)
            if curr_sum > max_sum:
                res_level = level
                max_sum = curr_sum
        return res_level


def main():
    pass


if __name__ == '__main__':
    main()
