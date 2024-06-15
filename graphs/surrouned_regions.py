# https://leetcode.com/problems/surrounded-regions/

from itertools import product


class Solution:
    def solve(self, board: list[list[str]]) -> None:
        used = set()

        def helper(i, j):
            used.add((i, j))
            if i in (0, len(board) - 1) or j in (0, len(board[0]) - 1):
                return False
            for x, y in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                if board[i + x][j + y] == 'X' or (i + x, j + y) in used:
                    continue
                if not helper(i + x, j + y):
                    return False
            return True

        marked = set()
        for i, j in product(range(len(board)), range(len(board[0]))):
            if board[i][j] == 'O' and (i, j) not in marked:
                if helper(i, j):
                    for x, y in used:
                        board[x][y] = 'X'
                else:
                    marked.union(used)
            used.clear()


class Solution2:
    def solve(self, board: list[list[str]]) -> None:
        m, n = len(board), len(board[0])

        def helper(i, j):
            board[i][j] = 'U'
            for x, y in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                if 0 <= i + x < m and 0 <= j + y < n and board[i + x][j + y] == 'O':
                    helper(i + x, j + y)

        for k in range(n):
            if board[0][k] == 'O':
                helper(0, k)
            if board[m - 1][k] == 'O':
                helper(m - 1, k)

        for k in range(m):
            if board[k][0] == 'O':
                helper(k, 0)
            if board[k][n - 1] == 'O':
                helper(k, n - 1)

        for i, j in product(range(m), range(n)):
            board[i][j] = 'O' if board[i][j] == 'U' else 'X'


def main():
    arr = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "O", "O", "X"], ["X", "O", "X", "X"]]
    print(Solution().solve(arr))


if __name__ == '__main__':
    main()
