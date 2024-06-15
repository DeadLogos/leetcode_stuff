# https://leetcode.com/problems/number-of-increasing-paths-in-a-grid/description/

from itertools import product
from functools import lru_cache


class Solution:
    def countPaths(self, grid: list[list[int]]) -> int:
        steps = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        n, m = len(grid), len(grid[0])

        @lru_cache(None)
        def helper(i, j):
            res = 1
            for x, y in steps:
                if 0 <= i + x < n and 0 <= j + y < m and grid[i + x][j + y] > grid[i][j]:
                    res += helper(i + x, j + y)
            return res

        ans = 0
        for i, j in product(range(n), range(m)):
            ans += helper(i, j)
        return ans % (10 ** 9 + 7)


class Solution2:
    def countPaths(self, grid: list[list[int]]) -> int:
        steps = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        n, m, total = len(grid), len(grid[0]), 0
        dp = [[1] * m for _ in range(n)]
        sorted_points = sorted(product(range(n), range(m)), key=lambda x: grid[x[0]][x[1]])
        for i, j in sorted_points:
            for x, y in steps:
                if 0 <= i + x < n and 0 <= j + y < m and grid[i + x][j + y] > grid[i][j]:
                    dp[i + x][j + y] += dp[i][j]
            total += dp[i][j]
        return total


def main():
    print(Solution2().countPaths([[2, 3], [3, 4]]))


if __name__ == '__main__':
    main()
