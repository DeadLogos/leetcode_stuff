# https://leetcode.com/problems/rotate-list/description/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None

        # считаем длину списка, чтобы обрезать лишние циклы
        total, right = 0, head
        while right and total < k:
            right = right.next
            total += 1
        if not right:
            k = k % total
            right = head
            for _ in range(k):
                right = right.next

        # ротейтим список, получив конец исходного и начала нового списка
        if not k:
            return head
        left = head
        while right.next:
            right, left = right.next, left.next
        new_head, left.next, right.next = left.next, None, head
        return new_head


def main():
    pass


if __name__ == '__main__':
    main()
