# https://leetcode.com/problems/linked-list-cycle-ii/
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # adding attribute index into object
    def detectCycle_change(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pos = 0
        node = head
        while node is not None:
            if hasattr(node, 'index'):
                return node.index
            node.index = pos
            pos += 1
            node = node.next
        return -1

    # using two indexes
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        while fast is not None and fast.next is not None:
            fast, slow = fast.next.next, slow.next
            if fast == slow:
                break
        else:
            return None
        node = head
        while node != slow:
            node = node.next
            slow = slow.next
        return node


def main():
    pass


if __name__ == '__main__':
    main()
