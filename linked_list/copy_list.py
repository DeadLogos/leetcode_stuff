# https://leetcode.com/problems/copy-list-with-random-pointer/description/

from typing import Optional


class Node:
    def __init__(self, x: int, next_=None, random=None):
        self.val = int(x)
        self.next = next_
        self.random = random

    def __repr__(self):
        return f'Node[{self.val}]'


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        copied_nodes = {}
        zero = node_copy = Node(0)
        node = head
        while node:
            node_copy.next = Node(node.val, random=node)
            copied_nodes[node] = node_copy.next
            node_copy, node = node_copy.next, node.next

        node_copy = zero.next
        while node_copy:
            node_copy.random = copied_nodes.get(node_copy.random.random)
            node_copy = node_copy.next
        return zero.next


class Solution2:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        copied_nodes = {}
        zero = node_copy = Node(0)
        node = head
        while node:
            node_copy.next = Node(node.val)
            copied_nodes[node] = node_copy.next
            node_copy, node = node_copy.next, node.next

        for node, node_copy in copied_nodes.items():
            node_copy.random = copied_nodes.get(node.random)
        return zero.next


class Solution3:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_map = {}
        node = head
        while node:
            node_map[node] = Node(node.val)
            node = node.next
        for node, node_copy in node_map.items():
            node_copy.next = node_map.get(node.next)
            node_copy.random = node_map.get(node.random)
        return node_map.get(head)


def main():
    root = Node(7)
    root.next = Node(10, random=root)
    root.next.next = Node(12, random=root.next)
    print(Solution().copyRandomList(root))


if __name__ == '__main__':
    main()
