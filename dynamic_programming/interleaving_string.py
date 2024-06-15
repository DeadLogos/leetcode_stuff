# https://leetcode.com/problems/interleaving-string/

from functools import lru_cache


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        @lru_cache(None)
        def helper(i, j, k):
            if k == len(s3):
                return True
            if i < len(s1) and s1[i] == s3[k] and helper(i + 1, j, k + 1):
                return True
            if j < len(s2) and s2[j] == s3[k] and helper(i, j + 1, k + 1):
                return True
            return False

        return helper(0, 0, 0)


class Solution2:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        dp[-1][-1] = True

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True
                if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True
        return dp[0][0]


def main():
    pass


if __name__ == '__main__':
    main()
