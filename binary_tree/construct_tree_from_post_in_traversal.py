# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> Optional[TreeNode]:
        def helper(inord, postord):
            if not inord:
                return
            i_vert = inord.index(postord[-1])
            left = helper(inord[:i_vert], postord[:i_vert])
            right = helper(inord[i_vert + 1:], postord[i_vert:-1])
            return TreeNode(val=postord[-1], left=left, right=right)

        return helper(inorder, postorder)


class Solution2:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> Optional[TreeNode]:
        inord_indexes = {val: i for i, val in enumerate(inorder)}

        def helper(l, r):
            if l > r:
                return
            node = TreeNode(postorder.pop())
            i_vert = inord_indexes[node.val]
            node.right = helper(i_vert + 1, r)
            node.left = helper(l, i_vert - 1)
            return node

        return helper(0, len(inorder) - 1)


class Solution3:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> Optional[TreeNode]:
        inord_indexes = {val: i for i, val in enumerate(inorder)}

        def helper(in_l, in_r, post_l, post_r):
            if in_l > in_r:
                return
            node = TreeNode(postorder[post_r])
            in_vert = inord_indexes[node.val]
            post_vert = post_l + (in_vert - in_l)
            node.left = helper(in_l, in_vert - 1, post_l, post_vert - 1)
            node.right = helper(in_vert + 1, in_r, post_vert, post_r - 1)
            return node

        return helper(0, len(inorder) - 1, 0, len(inorder) - 1)


def main():
    pass


if __name__ == '__main__':
    main()
