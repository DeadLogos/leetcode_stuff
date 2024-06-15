# https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/description/
from math import ceil


class Solution:
    @staticmethod
    def _count(l, r):
        ones = 0
        if l < 0:
            ones, l = -l, 0
        return (r * (r + 1) // 2 - l * (l + 1) // 2) + ones

    def max_value(self, n: int, indx: int, max_sum: int) -> int:
        left, right = ceil(max_sum / n), max_sum
        while left + 1 < right:
            middle = (left + right) // 2
            left_sum = self._count(middle - indx - 1, middle)
            right_sum = self._count(middle - n + indx, middle - 1)
            if left_sum + right_sum <= max_sum:
                left = middle
            else:
                right = middle
        return left


def main():
    print(Solution().max_value(3, 2, 18))


if __name__ == '__main__':
    main()
