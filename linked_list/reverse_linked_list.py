# https://leetcode.com/problems/reverse-linked-list/description/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head, reverse_pointer=None):
            if head is None:
                return reverse_pointer
            node = head.next
            head.next = reverse_pointer
            return reverse(node, head)
        return reverse(head)


def main():
    pass


if __name__ == '__main__':
    main()
