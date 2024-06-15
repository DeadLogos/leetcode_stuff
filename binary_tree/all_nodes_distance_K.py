# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/

from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> list[int]:
        def find(node, i=1, level=0):
            if node is None:
                return False
            if node == target:
                return i, level
            left = find(node.left, i * 2, level + 1)
            right = find(node.right, i * 2 + 1, level + 1)
            return left or right

        position, depth = find(root)
        self.left_bound, self.right_bound = 2 ** depth, 2 ** (depth + 1) - 1
        self.res = []

        def dfs(node, dist, is_direct=True):
            if node is None:
                return
            if not dist:
                is_direct = False
            if dist == k:
                self.res.append(node.val)
            if not is_direct:
                dfs(node.left, dist + 1, is_direct)
                dfs(node.right, dist + 1, is_direct)
            elif position - self.left_bound < self.right_bound - position:
                self.right_bound = (self.left_bound + self.right_bound) // 2
                dfs(node.left, dist - 1, is_direct)
                dfs(node.right, dist + 1, not is_direct)
            else:
                self.left_bound = (self.left_bound + self.right_bound) // 2 + 1
                dfs(node.left, dist + 1, not is_direct)
                dfs(node.right, dist - 1, is_direct)

        dfs(root, depth)
        return self.res


class Solution2:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> list[int]:
        def helper(node, parent):
            if node is None:
                return
            node.parent = parent
            helper(node.left, node)
            helper(node.right, node)

        helper(root, None)

        used = {target.val}
        deq, dist = deque([target]), 0
        while deq and dist < k:
            for _ in range(len(deq)):
                node = deq.popleft()
                if node.left and node.left.val not in used:
                    deq.append(node.left)
                    used.add(node.left.val)
                if node.right and node.right.val not in used:
                    deq.append(node.right)
                    used.add(node.right.val)
                if node.parent and node.parent.val not in used:
                    deq.append(node.parent)
                    used.add(node.parent.val)
            dist += 1
        return [node.val for node in deq]


def main():
    pass


if __name__ == '__main__':
    main()
