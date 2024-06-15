# https://leetcode.com/problems/knight-probability-in-chessboard/description/


from functools import lru_cache


class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        directions = [(1, 2), (1, -2), (-1, 2), (-1, -2),
                      (2, 1), (2, -1), (-2, 1), (-2, -1)]

        @lru_cache(None)
        def helper(i, j, remain_moves):
            if not 0 <= i < n or not 0 <= j < n:
                return 0
            if not remain_moves:
                return 1
            res = 0
            for i_d, j_d in directions:
                res += 0.125 * helper(i + i_d, j + j_d, remain_moves - 1)
            return res

        return helper(row, column, k)


def main():
    pass


if __name__ == '__main__':
    main()
