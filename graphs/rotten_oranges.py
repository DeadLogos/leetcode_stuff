# https://leetcode.com/problems/rotting-oranges/

from collections import deque
from itertools import product


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        m, n, total_fresh = len(grid), len(grid[0]), 0
        deq = deque()
        for i, j in product(range(m), range(n)):
            if grid[i][j] == 1:
                total_fresh += 1
            elif grid[i][j]:
                deq.append((i, j))

        min_left = 0
        while deq and total_fresh:
            for _ in range(len(deq)):
                i, j = deq.popleft()
                for x, y in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                    x, y = i + x, j + y
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                        deq.append((x, y))
                        grid[x][y] = 2
                        total_fresh -= 1
            min_left += 1
        return min_left if not total_fresh else -1


def main():
    pass


if __name__ == '__main__':
    main()
