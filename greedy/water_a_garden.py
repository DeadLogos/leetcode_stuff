# https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/


class Solution:
    def minTaps(self, n: int, ranges: list[int]) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(n + 1):
            left, right = max(0, i - ranges[i]), min(i + ranges[i], n)
            for j in range(left, right + 1):
                dp[right] = min(dp[j] + 1, dp[right])
        return dp[n] if dp[n] != float('inf') else -1


class Solution2:
    def minTaps(self, n: int, ranges: list[int]) -> int:
        jumps = [0] * (n + 1)
        for i in range(n + 1):
            left = max(0, i - ranges[i])
            right = min(n, i + ranges[i])
            jumps[left] = max(jumps[left], right - left)

        level = left = right = 0
        while right < n:
            next_right = right
            for i in range(left, right + 1):
                next_right = max(next_right, i + jumps[i])
            if next_right == right:
                return -1
            left, right = right + 1, next_right
            level += 1
        return level


class Solution3:
    def minTaps(self, n: int, ranges: list[int]) -> int:
        jumps = [0] * (n + 1)
        for i in range(n + 1):
            left = max(0, i - ranges[i])
            right = min(n, i + ranges[i])
            jumps[left] = max(jumps[left], right - left)

        taps = right = next_right = 0
        for i in range(n + 1):
            if i > next_right:
                return -1
            if i > right:
                right = next_right
                taps += 1
            next_right = max(next_right, i + jumps[i])
        return taps


def main():
    pass


if __name__ == '__main__':
    main()
