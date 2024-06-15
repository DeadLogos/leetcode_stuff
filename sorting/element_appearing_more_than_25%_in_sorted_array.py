# https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/

from bisect import bisect_left, bisect_right
from collections import Counter


class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:
        length = len(arr) // 4
        nums = (arr[length], arr[len(arr) // 2], arr[3 * len(arr) // 4])
        for num in nums:
            if (bisect_right(arr, num) - bisect_left(arr, num)) > length:
                return num


class Solution2:
    def findSpecialInteger(self, arr: list[int]) -> int:
        length = len(arr) // 4
        for i in range(len(arr) - length):
            if arr[i] == arr[i + length]:
                return arr[i]


class Solution3:
    def findSpecialInteger(self, arr: list[int]) -> int:
        res, res_x = 1, arr[0]
        curr, curr_x = 0, arr[0]
        for x in arr:
            if x != curr_x:
                curr, curr_x = 0, x
            curr += 1
            if curr > res:
                res, res_x = curr, curr_x
        return res_x


def main():
    pass


if __name__ == '__main__':
    main()
