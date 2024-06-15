# https://leetcode.com/problems/h-index/description/

import heapq
from collections import defaultdict


class Solution:
    def h_index_brute_force(self, cites: list[int]) -> int:
        h = 0
        total = len(cites)
        while h <= total and h <= len(cites):
            total = 0
            h += 1
            for x in cites:
                if x >= h:
                    total += 1
        return h - 1

    def h_index(self, cites: list[int]) -> int:
        cites.sort(reverse=True)
        for i, x in enumerate(cites, 1):
            if i > x:
                return i - 1
        return len(cites)

    def h_index_linear(self, cites: list[int]) -> int:
        n = len(cites)
        counter = [0] * (n + 1)
        for x in cites:
            counter[x if x < len(cites) else len(cites)] += 1
        i = 0
        for j, x in enumerate(counter):
            for _ in range(x):
                cites[i] = j
                i += 1
        cites.reverse()
        for i, x in enumerate(cites, 1):
            if i > x:
                return i - 1
        return len(cites)


class CurrentH:
    def __init__(self):
        self._arr = []
        heapq.heapify(self._arr)
        self._h_index = 0

    @property
    def h_index(self):
        return self._h_index

    def update_h_index(self, elem: int) -> int:
        if elem <= self._h_index:
            return self._h_index
        if self._arr and self._arr[0] == self._h_index:
            heapq.heappop(self._arr)
        else:
            self._h_index += 1
        heapq.heappush(self._arr, elem)
        return self._h_index


def main():
    # print(Solution().h_index_linear([2, 2, 3, 1, 4, 5, 3, 2, 4]))
    # print(Solution().h_index([2, 2, 3, 1, 4, 5, 3, 2, 4]))

    arr = [2, 6, 6, 3, 4, 4, 5, 10, 8, 3, 4, 7, 2, 6]
    h = CurrentH()
    for x in arr:
        curr = h.update_h_index(x)
        print(curr)
        print(h._arr)


if __name__ == '__main__':
    main()
