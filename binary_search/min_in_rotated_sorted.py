# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/


class Solution:
    def findMin(self, nums: list[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]
        left, right = 0, len(nums) - 1
        while left + 1 != right:
            middle = (left + right) // 2
            if nums[middle] > nums[left]:
                left = middle
            else:
                right = middle
        return nums[right]


class Solution2:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            middle = (left + right) // 2
            if nums[middle] > nums[right]:
                left = middle + 1
            else:
                right = middle
        return nums[left]


def main():
    pass


if __name__ == '__main__':
    main()
