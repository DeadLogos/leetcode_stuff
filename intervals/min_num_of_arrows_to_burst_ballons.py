# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/


class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort()
        res = 0
        last = float('-inf')
        for x, y in points:
            if x > last:
                res += 1
                last = y
            else:
                last = min(last, y)
        return res


def main():
    pass


if __name__ == '__main__':
    main()
