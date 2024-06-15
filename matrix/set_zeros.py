# https://leetcode.com/problems/set-matrix-zeroes/description/

from itertools import product
from math import inf


# O(n + m) space approach
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        zeros_rows, zeros_cols = set(), set()
        m, n = len(matrix), len(matrix[0])

        for i, j in product(range(m), range(n)):
            if not matrix[i][j]:
                zeros_rows.add(i)
                zeros_cols.add(j)

        for i in range(m):
            if i in zeros_rows:
                matrix[i][:] = [0] * n
            else:
                for j in zeros_cols:
                    matrix[i][j] = 0


# constant space approach
class Solution2:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        m, n = len(matrix), len(matrix[0])

        def helper(x, y):
            for k in range(m):
                matrix[k][y] = inf if matrix[k][y] else 0
            for k in range(n):
                matrix[x][k] = inf if matrix[x][k] else 0

        print(*matrix, sep='\n')
        print()
        for i, j in product(range(m), range(n)):
            if not matrix[i][j]:
                helper(i, j)
                print(*matrix, sep='\n')
                print()

        for i, j in product(range(m), range(n)):
            if matrix[i][j] == inf:
                matrix[i][j] = 0


class Solution3:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        zero_col = zero_row = False

        for i, j in product(range(m), range(n)):
            if not matrix[i][j]:
                if i:
                    matrix[i][0] = 0
                else:
                    zero_row = True
                if j:
                    matrix[0][j] = 0
                else:
                    zero_col = True

        for i, j in product(range(1, m), range(1, n)):
            if not matrix[i][0] or not matrix[0][j]:
                matrix[i][j] = 0

        if zero_row:
            matrix[0][:] = [0] * n
        if zero_col:
            for i in range(m):
                matrix[i][0] = 0


def main():
    arr = [[1, 2, 3, 4], [5, 0, 7, 8], [0, 10, 11, 12], [13, 14, 15, 0]]
    Solution2().setZeroes(arr)

    print(*arr, sep='\n')


if __name__ == '__main__':
    main()
