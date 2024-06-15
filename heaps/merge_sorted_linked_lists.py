# https://leetcode.com/problems/merge-k-sorted-lists/submissions/965951649/

import heapq
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# using min heap
class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(arr, (node.val, i))
                lists[i] = lists[i].next
        res = curr = ListNode()
        while arr:
            value, i = heapq.heappop(arr)
            curr.next = ListNode(val=value)
            curr = curr.next
            if lists[i]:
                heapq.heappush(arr, (lists[i].val, i))
                lists[i] = lists[i].next
        return res.next


# using kinda merge sort approach(divide and conquer)
class Solution2:
    def mergeKLists(self, arr: list[Optional[ListNode]]) -> Optional[ListNode]:
        if not arr:
            return None

        while len(arr) != 1:
            curr = 0
            for i in range(0, len(arr), 2):
                arr[curr] = self.merge_two_lists(arr[i], arr[i + 1] if i + 1 < len(arr) else None)
                curr += 1
            while len(arr) != curr:
                del arr[-1]
        return arr[0]

    def merge_two_lists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        first = last = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                last.next = list1
                list1 = list1.next
            else:
                last.next = list2
                list2 = list2.next
            last = last.next
        last.next = list1 if list2 is None else list2
        return first.next


def main():
    pass


if __name__ == '__main__':
    main()
