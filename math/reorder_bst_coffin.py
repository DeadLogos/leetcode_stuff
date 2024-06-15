# https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/description/


from functools import lru_cache
from typing import Optional
from math import factorial as fct


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def add_node(root: TreeNode, node: TreeNode):
    curr, parent = root, None
    while curr:
        parent = curr
        curr = curr.left if node.val < curr.val else curr.right
    if node.val < parent.val:
        parent.left = node
    else:
        parent.right = node


# very bad solution
class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        root = TreeNode(nums[0])
        nodes = {nums[0]: root}
        for i in range(1, len(nums)):
            nodes[nums[i]] = TreeNode(nums[i])
            add_node(root, nodes[nums[i]])

        res = [-1]

        def helper(ways: set):
            if not ways:
                res[0] += 1
                return 1

            for value in ways.copy():
                ways.discard(value)
                node = nodes[value]
                if node.left:
                    ways.add(node.left.val)
                if node.right:
                    ways.add(node.right.val)

                helper(ways)

                ways.add(value)
                if node.left:
                    ways.discard(node.left.val)
                if node.right:
                    ways.discard(node.right.val)

        helper({root.val})
        return res[0]


# перестановки с повторением, а не бином
class Solution2:
    def numOfWays(self, nums: list[int]) -> int:
        def helper(arr):
            if len(arr) <= 2:
                return 1

            left_arr, right_arr = [], []
            for x in arr:
                if x < arr[0]:
                    left_arr.append(x)
                elif x > arr[0]:
                    right_arr.append(x)

            coefficient = fct(len(arr) - 1) // (fct(len(left_arr)) * fct(len(right_arr)))
            return coefficient * helper(left_arr) * helper(right_arr)

        return (helper(nums) - 1) % (10 ** 9 + 7)


def main():
    arr = [3, 5, 4, 6, 1, 2]
    print(Solution2().numOfWays(arr))


if __name__ == '__main__':
    main()
