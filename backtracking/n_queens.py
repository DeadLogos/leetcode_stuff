# https://leetcode.com/problems/n-queens/

from typing import Optional


class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        grid, res = [['.'] * n for _ in range(n)], []
        cols, right_diag, left_diag = set(), set(), set()

        def back_track(row):
            if row == n:
                res.append(list(map(lambda x: ''.join(x), grid)))
                return

            for col in range(n):
                if col in cols or row + col in right_diag or row - col in left_diag:
                    continue

                grid[row][col] = 'Q'
                cols.add(col)
                right_diag.add(row + col)
                left_diag.add(row - col)

                back_track(row + 1)

                grid[row][col] = '.'
                cols.discard(col)
                right_diag.discard(row + col)
                left_diag.discard(row - col)

        back_track(0)
        return res


def main():
    pass


if __name__ == '__main__':
    main()
