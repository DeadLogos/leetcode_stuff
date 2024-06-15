# https://leetcode.com/problems/swap-nodes-in-pairs/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'Node[{self.val}] -> {self.next}'


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        zero = prev = ListNode(next=head)
        while node and node.next:
            second_node = node.next

            prev.next = second_node
            node.next = second_node.next
            second_node.next = node

            prev = node
            node = node.next
        return zero.next


# recursive
class Solution2:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def helper(node: Optional[ListNode]):
            if node is None or node.next is None:
                return node
            second = node.next
            node.next = helper(second.next)
            second.next = node
            return second

        return helper(head)


def main():
    root = ListNode(1)
    root.next = ListNode(2)
    root.next.next = ListNode(3)
    root.next.next.next = ListNode(4)

    print(root)
    print(Solution().swapPairs(root))


if __name__ == '__main__':
    main()
