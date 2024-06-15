# https://leetcode.com/problems/last-stone-weight/

import heapq


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            elem1 = heapq.heappop(stones)
            elem2 = heapq.heappop(stones)
            if elem1 != elem2:
                heapq.heappush(stones, elem1 - elem2)
        return -stones[0] if stones else 0


def main():
    pass


if __name__ == '__main__':
    main()
