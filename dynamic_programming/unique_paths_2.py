# https://leetcode.com/problems/unique-paths-ii/

from itertools import product


class Solution:
    def uniquePathsWithObstacles(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(n):
            if grid[0][i]:
                break
            dp[0][i] = 1
        for i in range(m):
            if grid[i][0]:
                break
            dp[i][0] = 1

        for i, j in product(range(1, m), range(1, n)):
            dp[i][j] = (dp[i - 1][j] if not grid[i - 1][j] else 0) + (dp[i][j - 1] if not grid[i][j - 1] else 0)
        return dp[-1][-1] if not grid[-1][-1] else 0


def main():
    arr = [[0, 0, 0, 0, 0],
           [0, 1, 0, 0, 0],
           [1, 0, 0, 0, 0],
           [0, 0, 0, 1, 0],
           [0, 0, 0, 0, 0]]
    print(Solution().uniquePathsWithObstacles(arr))


if __name__ == '__main__':
    main()
