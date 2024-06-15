# https://leetcode.com/problems/single-number-ii/description/


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        nums.sort()
        for i in range(0, len(nums), 3):
            if i == len(nums) - 1 or nums[i + 1] != nums[i]:
                return nums[i]


def main():
    pass


if __name__ == '__main__':
    main()
