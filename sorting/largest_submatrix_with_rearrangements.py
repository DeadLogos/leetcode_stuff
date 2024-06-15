# https://leetcode.com/problems/largest-submatrix-with-rearrangements/


class Solution:
    def largestSubmatrix(self, matrix: list[list[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        res = 0
        dp = [0] * n
        for row in matrix:
            for i in range(n):
                dp[i] = 0 if not row[i] else dp[i] + 1
            for j, x in enumerate(sorted(dp, reverse=True)):
                res = max(res, x * (j + 1))
        return res


def main():
    pass


if __name__ == '__main__':
    main()
