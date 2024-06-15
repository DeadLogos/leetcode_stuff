# https://leetcode.com/problems/equal-row-and-column-pairs/

from collections import defaultdict


class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        cache = defaultdict(lambda: 0)
        for row in grid:
            cache[tuple(row)] += 1

        n = len(grid)
        for i in range(n):
            for j in range(i + 1, n):
                grid[i][j], grid[j][i] = grid[j][i], grid[i][j]

        res = 0
        for row in grid:
            res += cache[tuple(row)]
        return res


class Solution1:
    def equalPairs(self, grid: list[list[int]]) -> int:
        cache = defaultdict(lambda: 0)
        for row in grid:
            cache[tuple(row)] += 1

        res = 0
        for row in zip(*grid):
            res += cache[tuple(row)]
        return res


# no additional memory
class Solution2:
    def equalPairs(self, grid: list[list[int]]) -> int:
        n = len(grid)
        res = 0
        for i in range(n):
            for j in range(n):
                for x in range(n):
                    if grid[i][x] != grid[x][j]:
                        break
                else:
                    res += 1


def main():
    pass


if __name__ == '__main__':
    main()
