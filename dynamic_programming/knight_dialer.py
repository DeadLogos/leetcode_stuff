# https://leetcode.com/problems/knight-dialer/


class Solution:
    jumps = [
        (4, 6),
        (6, 8),
        (7, 9),
        (4, 8),
        (3, 9, 0),
        (),
        (1, 7, 0),
        (2, 6),
        (1, 3),
        (2, 4)
    ]

    def knightDialer(self, n: int) -> int:
        dp = [1] * len(self.jumps)
        for _ in range(n - 1):
            last_dp = dp.copy()
            for i in range(len(dp)):
                dp[i] = sum(last_dp[j] for j in self.jumps[i])
        return sum(dp) % (10 ** 9 + 7)


def main():
    pass


if __name__ == '__main__':
    main()
