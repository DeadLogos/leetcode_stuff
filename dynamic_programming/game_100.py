# https://leetcode.com/problems/can-i-win/

from functools import lru_cache


class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if maxChoosableInteger * (maxChoosableInteger + 1) // 2 < desiredTotal:
            return False

        @lru_cache(None)
        def helper(desired_point: int, rest_moves: tuple):
            if rest_moves[-1] >= desired_point:
                return True
            for i, move in enumerate(rest_moves):
                if not helper(desired_point - move, rest_moves[:i] + rest_moves[i + 1:]):
                    return True
            return False

        return helper(desiredTotal, tuple(range(1, maxChoosableInteger + 1)))


def main():
    print(Solution().canIWin(10, 21))


if __name__ == '__main__':
    main()
