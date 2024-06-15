# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        zero = prev = ListNode(next=head)
        slow = fast = head
        while fast and fast.next:
            prev, slow = slow, slow.next
            fast = fast.next.next
        prev.next = slow.next
        return zero.next


def main():
    pass


if __name__ == '__main__':
    main()
