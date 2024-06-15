# https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/


class Solution:
    def getSumAbsoluteDifferences(self, nums: list[int]) -> list[int]:
        res = [sum(abs(nums[0] - x) for x in nums)]
        for i in range(1, len(nums)):
            sum_abs_diff = (res[-1] + abs(nums[i] - nums[i - 1]) * (2 * i - len(nums)))
            res.append(sum_abs_diff)
        return res


def main():
    pass


if __name__ == '__main__':
    main()
