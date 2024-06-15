# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/description/


class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        i, j = 0, len(grid[0]) - 1
        res = 0
        while i < len(grid) and j >= 0:
            if grid[i][j] >= 0:
                i += 1
            else:
                res += len(grid) - i
                j -= 1
        return res


def main():
    pass


if __name__ == '__main__':
    main()
