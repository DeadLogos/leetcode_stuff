# https://leetcode.com/problems/split-linked-list-in-parts/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> list[Optional[ListNode]]:
        length, node = 0, head
        while node:
            length += 1
            node = node.next
        part_len, i = length // k + 1, length % k

        res, node = [], head
        for _ in range(k):
            if len(res) == i:
                part_len -= 1
            zero = curr = ListNode()
            for __ in range(part_len):
                curr.next = node
                node.next, node = None, node.next
                curr = curr.next
            res.append(zero.next)
        return res


def main():
    pass


if __name__ == '__main__':
    main()
