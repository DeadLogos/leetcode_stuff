# https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/

from functools import lru_cache


class Solution:
    def minInsertions(self, s: str) -> int:
        @lru_cache(None)
        def helper(i, j):
            while i < j and s[i] == s[j]:
                i += 1
                j -= 1
            return 0 if i >= j else min(helper(i + 1, j), helper(i, j - 1)) + 1

        return helper(0, len(s) - 1)


class Solution2:
    def minInsertions(self, s: str) -> int:
        dp = [[0] * len(s) for _ in range(len(s))]

        for step in range(len(s) - 1, 0, -1):
            for i in range(step):
                j = len(s) - step + i
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = min(dp[i + 1][j], dp[i][j - 1]) + 1
        return dp[0][-1]


def main():
    pass


if __name__ == '__main__':
    main()
