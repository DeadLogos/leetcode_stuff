# https://leetcode.com/problems/counting-bits/


class Solution:
    def countBits(self, n: int) -> list[int]:
        res = [0]
        while len(res) <= n:
            for i in range(0, len(res)):
                res.append(res[i] + 1)
        return res[:n + 1]


class Solution2:
    def countBits(self, n: int) -> list[int]:
        dp = [0] * (n + 1)
        offset = 1
        for i in range(1, n + 1):
            if 2 * offset == i:
                offset *= 2
            dp[i] = dp[i - offset] + 1
        return dp


def main():
    pass


if __name__ == '__main__':
    main()
