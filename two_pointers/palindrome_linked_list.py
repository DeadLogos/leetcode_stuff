# https://leetcode.com/problems/palindrome-linked-list/description/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_

    def __repr__(self):
        return f'Node({self.val}) -> {self.next}'


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse(hd: Optional[ListNode]) -> Optional[ListNode]:
            pointer = None
            curr = hd
            while curr:
                node = curr
                curr = curr.next
                node.next = pointer
                pointer = node
            return pointer

        slow = fast = head
        while fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next

        slow.next = reverse(slow.next)

        left, right = head, slow.next
        while right:
            if left.val != right.val:
                slow.next = reverse(slow.next)
                return False
            left, right = left.next, right.next
        slow.next = reverse(slow.next)
        return True


class Solution2:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse(first: Optional[ListNode], pointer: Optional[ListNode] = None) -> Optional[ListNode]:
            if first is None:
                return pointer
            node = first.next
            first.next = pointer
            return reverse(node, first)

        slow = fast = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        slow.next = reverse(slow.next)

        left, right = head, slow.next
        while right:
            if left.val != right.val:
                slow.next = reverse(slow.next)  # обратный реверс
                return False
            left = left.next
            right = right.next
        slow.next = reverse(slow.next)
        return True


def main():
    arr = [1, 7, 2, 2, 7, 1]
    zero = root = ListNode()
    for x in arr:
        root.next = ListNode(x)
        root = root.next
    print(zero.next)
    print(Solution().isPalindrome(zero.next))
    print(zero.next)


if __name__ == '__main__':
    main()
