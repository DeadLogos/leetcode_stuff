# https://leetcode.com/problems/add-two-numbers/description/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_

    def __repr__(self):
        return f'Node[{self.val}] -> {self.next}'


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        zero = node = ListNode()
        p1, p2, carry = l1, l2, 0
        while p1 or p2 or carry:
            carry, digit = divmod((p1.val if p1 else 0) + (p2.val if p2 else 0) + carry, 10)
            node.next = ListNode(digit)
            node = node.next
            p1, p2 = p1.next if p1 else p1, p2.next if p2 else p2
        return zero.next


def main():
    arr1 = [4, 5, 7, 8]
    arr2 = [6, 8, 7, 8, 3]

    dummy = root = ListNode()
    for x in arr1:
        root.next = ListNode(x)
        root = root.next
    l1 = dummy.next

    dummy = root = ListNode()
    for x in arr2:
        root.next = ListNode(x)
        root = root.next
    l2 = dummy.next
    print(l1)
    print(l2)

    l3 = Solution().addTwoNumbers(l1, l2)
    print(l3)


if __name__ == '__main__':
    main()
