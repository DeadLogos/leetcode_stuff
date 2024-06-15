# https://leetcode.com/problems/domino-and-tromino-tiling/


class Solution:
    def numTilings(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            for j in range(i):
                dp[i] += dp[j] * (2 if j < i - 2 else 1)
        return dp[-1] % (10 ** 9 + 7)


class Solution2:
    def numTilings(self, n: int) -> int:
        pre_sum, prev, curr = 0, 1, 1
        for i in range(n - 1):
            pre_sum, prev, curr = pre_sum + prev, curr, pre_sum * 2 + prev + curr
        return curr % (10 ** 9 + 7)


def main():
    pass


if __name__ == '__main__':
    main()
