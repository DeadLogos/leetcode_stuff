# https://leetcode.com/problems/merge-intervals/description/


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            if intervals[i][0] <= res[-1][1]:
                res[-1][1] = max(intervals[i][1], res[-1][1])
            else:
                res.append(intervals[i])

        return res


class Solution2:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        def merge_two_intervals(prev, curr):
            return prev[0], max(prev[1], curr[1])

        def is_overlapped(prev, curr):
            return curr[0] <= prev[1]

        res = []
        intervals.sort()
        prev_interval = intervals[0]

        for curr_interval in intervals:
            if is_overlapped(prev_interval, curr_interval):
                prev_interval = merge_two_intervals(prev_interval, curr_interval)
            else:
                res.append(prev_interval)
                prev_interval = curr_interval
        res.append(prev_interval)
        return res


def main():
    pass


if __name__ == '__main__':
    main()
