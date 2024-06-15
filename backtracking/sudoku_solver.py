# https://leetcode.com/problems/sudoku-solver/

from typing import Optional


class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        def is_safe(i, j, digit):
            for x in range(len(board)):
                if board[x][j] == str(digit):
                    return False
                if board[i][x] == str(digit):
                    return False
            x_0, y_0 = 3 * (i // 3), 3 * (j // 3)
            for x in range(x_0, x_0 + 3):
                for y in range(y_0, y_0 + 3):
                    if board[x][y] == str(digit):
                        return False
            return True

        def backtracking(i, j):
            if i == len(board):
                return True
            if j == len(board):
                return backtracking(i + 1, 0)
            if board[i][j] == '.':
                for digit in range(1, len(board) + 1):
                    if is_safe(i, j, digit):
                        board[i][j] = str(digit)
                        if backtracking(i, j + 1):
                            return True
                        board[i][j] = '.'
                return False
            else:
                return backtracking(i, j + 1)

        backtracking(0, 0)


def main():
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    Solution().solveSudoku(board)

    print(*board, sep='\n')


if __name__ == '__main__':
    main()
