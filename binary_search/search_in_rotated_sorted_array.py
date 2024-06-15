# https://leetcode.com/problems/search-in-rotated-sorted-array


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums)
        while l + 1 < r:
            middle = (l + r) // 2
            if nums[middle] > nums[l]:
                l = middle
            else:
                r = middle

        left, right = (0, l) if target >= nums[0] else (r, len(nums) - 1)
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        return -1


def main():
    pass


if __name__ == '__main__':
    main()
