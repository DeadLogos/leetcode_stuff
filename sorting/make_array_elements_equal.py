# https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/


class Solution:
    def reductionOperations(self, nums: list[int]) -> int:
        nums.sort()
        curr_level = res = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                curr_level += 1
            res += curr_level
        return res


def main():
    pass


if __name__ == '__main__':
    main()
