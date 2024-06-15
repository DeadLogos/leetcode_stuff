# https://leetcode.com/problems/delete-node-in-a-bst

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def delete_node_with_two_child(node):
        leftmost_node, parent = node.right, node
        while leftmost_node.left:
            leftmost_node, parent = leftmost_node.left, leftmost_node
        node.val = leftmost_node.val
        setattr(parent, 'left' if parent != node else 'right', leftmost_node.left or leftmost_node.right)

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        parent, node, branch = None, root, 'left'
        while node:
            if node.val == key:
                break
            parent = node
            node, branch = (node.left, 'left') if node.val > key else (node.right, 'right')
        else:
            return root

        if node.left and node.right:
            self.delete_node_with_two_child(node)
        elif node != root:
            setattr(parent, branch, node.left or node.right)
        else:
            root = root.left or root.right
        return root


class Solution2:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif not root.left or not root.right:
            return root.left or root.right
        else:
            leftmost_node = root.right
            while leftmost_node.left:
                leftmost_node = leftmost_node.left
            root.val = leftmost_node.val
            root.right = self.deleteNode(root.right, leftmost_node.val)
        return root


def main():
    pass


if __name__ == '__main__':
    main()
