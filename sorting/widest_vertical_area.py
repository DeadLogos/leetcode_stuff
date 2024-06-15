# https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/


class Solution:
    def maxWidthOfVerticalArea(self, points: list[list[int]]) -> int:
        x_points = sorted(map(lambda p: p[0], points))
        res = 0
        for i in range(1, len(points)):
            res = max(res, x_points[i] - x_points[i - 1])
        return res


def main():
    pass


if __name__ == '__main__':
    main()
