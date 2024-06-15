# https://leetcode.com/problems/maximum-running-time-of-n-computers/description/


class Solution:
    def maxRunTime(self, n: int, batteries: list[int]) -> int:
        batteries.sort()
        inserted = batteries[-n:]
        rest = sum(batteries[:-n])
        for i in range(n - 1):
            refill = (i + 1) * (inserted[i + 1] - inserted[i])

            if rest < refill:
                return inserted[i] + rest // (i + 1)

            rest -= refill
        return inserted[-1] + rest // n


def main():
    pass


if __name__ == '__main__':
    main()
