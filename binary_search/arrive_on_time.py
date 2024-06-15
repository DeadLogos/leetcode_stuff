# https://leetcode.com/problems/minimum-speed-to-arrive-on-time/description/

from math import ceil


class Solution:
    def is_appropriate_speed(self, dist, speed, required_time):
        hour = 0
        for ride in dist:
            hour = ceil(hour)
            hour += ride / speed
        return hour <= required_time

    def minSpeedOnTime(self, dist: list[int], hour: float) -> int:
        left, right = 0, 10 ** 7 + 1
        while left + 1 < right:
            middle_speed = (left + right) // 2
            if self.is_appropriate_speed(dist, middle_speed, hour):
                right = middle_speed
            else:
                left = middle_speed
        return right if right != 10 ** 7 + 1 else -1


def main():
    pass


if __name__ == '__main__':
    main()
