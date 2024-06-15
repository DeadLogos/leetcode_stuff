# https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/description/


class Solution:
    def longestSubsequence(self, arr: list[int], difference: int) -> int:
        dp = {}
        res = 0
        for x in arr:
            dp[x] = dp.get(x - difference, 0) + 1
            res = max(res, dp[x])
        return res


def main():
    pass


if __name__ == '__main__':
    main()
