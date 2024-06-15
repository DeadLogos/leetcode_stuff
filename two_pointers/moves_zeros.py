# https://leetcode.com/problems/move-zeroes/


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        for i in range(len(nums)):
            if not nums[i]:
                left, right = i, i + 1
                break
        else:
            return

        while right < len(nums):
            if nums[right]:
                nums[left], nums[right] = nums[right], 0
                left += 1
            right += 1


class Solution2:
    def moveZeroes(self, nums: list[int]) -> None:
        left = 0
        for right in range(len(nums)):
            if nums[right]:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1


def main():
    pass


if __name__ == '__main__':
    main()
