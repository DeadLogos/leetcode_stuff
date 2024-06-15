# https://leetcode.com/problems/odd-even-linked-list/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        zero1 = odd = ListNode()
        zero2 = even = ListNode()
        node = head
        while node and node.next:
            odd.next = node
            even.next = node.next
            odd, even = odd.next, even.next
            node = node.next.next
        if node:
            odd.next = node
            odd = odd.next
        odd.next, even.next = zero2.next, None
        return zero1.next



def main():
    pass


if __name__ == '__main__':
    main()
