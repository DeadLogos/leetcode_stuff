# https://leetcode.com/problems/single-number/description/


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        x = nums[0]
        for i in range(1, len(nums)):
            x ^= nums[i]
        return x


def main():
    pass


if __name__ == '__main__':
    main()
