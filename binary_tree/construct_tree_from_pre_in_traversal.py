# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        def helper(pre, inord):
            curr = TreeNode(pre[0])
            root_index = inord.index(pre[0])

            if root_index:
                curr.left = helper(pre[1:root_index + 1], inord[:root_index])

            if root_index + 1 != len(pre):
                curr.right = helper(pre[root_index + 1:], inord[root_index + 1:])

            return curr

        return helper(preorder, inorder)


def main():
    pass


if __name__ == '__main__':
    main()
