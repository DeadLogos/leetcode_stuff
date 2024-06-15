# https://leetcode.com/problems/minimum-time-visiting-all-points/


class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        res = 0
        for i in range(1, len(points)):
            x, y = abs(points[i][0] - points[i - 1][0]), abs(points[i][1] - points[i - 1][1])
            res += max(x, y)
        return res


def main():
    pass


if __name__ == '__main__':
    main()
