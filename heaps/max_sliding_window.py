# https://leetcode.com/problems/sliding-window-maximum/

import heapq
from typing import Optional, Iterable
from collections import deque


class MaxHeap:
    def __init__(self, data: Optional[Iterable[tuple[int, int]]] = None) -> None:
        self.data = [(-x, i) for x, i in data] if data else []
        heapq.heapify(self.data)

    def __bool__(self):
        return bool(self.data)

    @property
    def max(self):
        return -self.data[0][0], self.data[0][1]

    def add(self, elem):
        heapq.heappush(self.data, (-elem[0], elem[1]))

    def pop(self):
        x, i = heapq.heappop(self.data)
        return -x, i


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        heap = MaxHeap([(x, i) for i, x in enumerate(nums[:k])])
        res = [heap.max[0]]
        for i in range(k, len(nums)):
            while heap and heap.max[1] <= i - k:
                heap.pop()
            heap.add((nums[i], i))
            res.append(heap.max[0])
        return res


class Solution2:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        deq = deque()
        res = []
        for i in range(len(nums)):
            while deq and nums[deq[-1]] < nums[i]:
                deq.pop()
            deq.append(i)
            if i + 1 >= k:
                res.append(nums[deq[0]])
                if deq[0] == i - k + 1:
                    deq.popleft()
        return res


def main():
    pass


if __name__ == '__main__':
    main()
