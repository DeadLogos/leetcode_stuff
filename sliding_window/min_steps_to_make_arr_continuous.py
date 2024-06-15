# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/


class Solution:
    def minOperations(self, nums: list[int]) -> int:
        snums = sorted(set(nums))
        max_close = 1
        l = r = 0
        while r < len(snums):
            while l < r and snums[r] - snums[l] > len(nums) - 1:
                l += 1
            max_close = max(max_close, r - l + 1)
            r += 1
        return len(nums) - max_close


def main():
    pass


if __name__ == '__main__':
    main()
