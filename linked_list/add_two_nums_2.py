# https://leetcode.com/problems/add-two-numbers-ii

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, node = '', l1
        while node:
            num1 += str(node.val)
            node = node.next

        num2, node = '', l2
        while node:
            num2 += str(node.val)
            node = node.next

        res = str(int(num1) + int(num2))
        zero = node = ListNode()
        for digit in res:
            node.next = ListNode(int(digit))
            node = node.next
        return zero.next


class Solution2:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, node = [], l1
        while node:
            num1.append(node.val)
            node = node.next

        num2, node = [], l2
        while node:
            num2.append(node.val)
            node = node.next

        carry = 0
        node = ListNode(carry)
        while num1 or num2 or carry:
            if num1:
                node.val += num1.pop()
            if num2:
                node.val += num2.pop()
            carry, node.val = divmod(node.val, 10)
            node = ListNode(carry, node)
        return node.next


def main():
    pass


if __name__ == '__main__':
    main()
