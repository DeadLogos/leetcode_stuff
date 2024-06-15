# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        left, right = -1, len(nums)
        while left + 1 < right:
            middle = (left + right) // 2
            if nums[middle] >= target:
                right = middle
            else:
                left = middle
        left_bound = left

        left, right = -1, len(nums)
        while left + 1 < right:
            middle = (left + right) // 2
            if nums[middle] <= target:
                left = middle
            else:
                right = middle
        right_bound = right

        return [left_bound + 1, right_bound - 1] if left_bound + 1 < right_bound else [-1, -1]


def get_max_length_of_continuous_seq(arr: list[int]):
    res = curr = 1
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1] + 1:
            curr = 0
        curr += 1
        res = max(res, curr)
    return max(res, curr)


def main():
    print(get_max_length_of_continuous_seq(list(map(int, input().split()))))


if __name__ == '__main__':
    main()
