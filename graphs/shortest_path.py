# https://leetcode.com/problems/shortest-path-in-binary-matrix/

from collections import deque
from itertools import product


class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        if not grid or grid[0][0]:
            return -1
        n = len(grid)
        used = {(0, 0)}
        deq = deque([(0, 0, 1)])
        while deq:
            x, y, length = deq.popleft()
            if x == y == n - 1:
                return length
            for step in product(range(-1, 2), range(-1, 2)):
                i, j = x + step[0], y + step[1]
                if 0 <= i < n and 0 <= j < n and (i, j) not in used and not grid[i][j]:
                    deq.append((i, j, length + 1))
                    used.add((i, j))
        return -1


def main():
    pass


if __name__ == '__main__':
    main()
