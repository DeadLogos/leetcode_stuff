# https://leetcode.com/problems/sort-array-by-parity/


class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        left, right = 0, len(nums) - 1
        while left < right:
            if not nums[left] % 2:
                left += 1
            elif nums[right] % 2:
                right -= 1
            else:
                nums[left], nums[right] = nums[right], nums[left]
        return nums


class Solution2:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        left = 0
        for right in range(len(nums)):
            if not nums[right] % 2:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        return nums


def main():
    pass


if __name__ == '__main__':
    main()
