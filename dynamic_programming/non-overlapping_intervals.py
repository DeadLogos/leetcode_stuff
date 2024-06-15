# https://leetcode.com/problems/non-overlapping-intervals/

from bisect import bisect_left
from functools import lru_cache


class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort()
        res = 0

        @lru_cache(None)
        def helper(i):
            if i == len(intervals):
                return 0

            next_i = bisect_left(intervals, intervals[i][1], key=lambda x: x[0])
            return max(helper(i + 1), 1 + helper(next_i))

        return len(intervals) - helper(0)


class Solution2:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort()
        res = 0
        left = 0
        for right in range(1, len(intervals)):
            if intervals[right][0] < intervals[left][1]:
                res += 1
                if intervals[right][1] < intervals[left][1]:
                    left = right
                continue
            left = right
        return res


def main():
    pass


if __name__ == '__main__':
    main()
