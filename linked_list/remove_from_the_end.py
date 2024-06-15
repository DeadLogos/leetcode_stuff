# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        total, node = 0, head
        while node:
            total += 1
            node = node.next

        zero = ListNode(next=head)
        prev, node = zero, head
        for _ in range(total - n):
            prev, node = prev.next, node.next
        prev.next = node.next
        return zero.next


# one path
class Solution2:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        zero = ListNode(next=head)
        left, right = zero, head
        for _ in range(n):
            right = right.next
        while right:
            left, right = left.next, right.next
        left.next = left.next.next
        return zero.next


def main():
    pass


if __name__ == '__main__':
    main()
