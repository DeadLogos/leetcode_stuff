# https://leetcode.com/problems/partition-list

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        zero1 = left = ListNode()
        zero2 = prev = ListNode(next=head)
        curr = head
        while curr:
            if curr.val < x:
                left.next = curr
                prev.next = curr.next
                left = left.next
            else:
                prev = prev.next
            curr = curr.next
        left.next = zero2.next
        return zero1.next


def main():
    pass


if __name__ == '__main__':
    main()
