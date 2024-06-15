# https://leetcode.com/problems/find-peak-element/


class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if (not mid or nums[mid - 1] < nums[mid]) and (mid == len(nums) - 1 or nums[mid + 1] < nums[mid]):
                return mid
            elif mid and nums[mid - 1] > nums[mid]:
                right = mid - 1
            else:
                left = mid + 1


def main():
    pass


if __name__ == '__main__':
    main()
