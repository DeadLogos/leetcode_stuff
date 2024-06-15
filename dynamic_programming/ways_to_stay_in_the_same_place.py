# https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/

from functools import lru_cache


class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        @lru_cache(None)
        def helper(i, remaining_steps):
            if i < 0 or i == arrLen:
                return 0
            if remaining_steps == 0:
                return i == 0

            st = remaining_steps - 1
            return helper(i - 1, st) + helper(i, st) + helper(i + 1, st)

        return helper(0, steps) % (10 ** 9 + 7)


class Solution2:
    def numWays(self, steps: int, arrLen: int) -> int:
        arrLen = min(arrLen, steps)
        dp = [0, 1] + [0] * arrLen
        for _ in range(steps):
            new_dp = [0] * len(dp)
            for i in range(1, len(dp) - 1):
                new_dp[i] = dp[i - 1] + dp[i] + dp[i + 1]
            dp = new_dp
        return dp[1] % (10 ** 9 + 7)


def main():
    pass


if __name__ == '__main__':
    main()
