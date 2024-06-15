# https://leetcode.com/problems/01-matrix/

from collections import deque


class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        m, n = len(mat), len(mat[0])
        res = [[float('inf')] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if not mat[i][j]:
                    res[i][j] = 0
                else:
                    top = res[i - 1][j] if i else float('inf')
                    left = res[i][j - 1] if j else float('inf')
                    res[i][j] = min(top, left) + 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if mat[i][j]:
                    bottom = res[i + 1][j] if i < m - 1 else float('inf')
                    right = res[i][j + 1] if j < n - 1 else float('inf')
                    res[i][j] = min(res[i][j], min(bottom, right) + 1)
        return res


class Solution2:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        m, n = len(mat), len(mat[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        res = mat.copy()
        deq = deque()

        for i in range(m):
            for j in range(n):
                if not res[i][j]:
                    deq.append((i, j))
                else:
                    mat[i][j] = -1

        while deq:
            i, j = deq.popleft()
            for x, y in directions:
                x, y = i + x, j + y
                if 0 <= x < m and 0 <= y < n and mat[x][y] == -1:
                    res[x][y] = res[i][j] + 1
                    deq.append((x, y))

        return res


def main():
    pass


if __name__ == '__main__':
    main()
