# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/


class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        left = right = res = 0
        zero_pos = None
        while right < len(nums):
            if not nums[right]:
                left = zero_pos + 1 if zero_pos is not None else left
                zero_pos = right
            res = max(right - left, res)
            right += 1
        return res


def main():
    pass


if __name__ == '__main__':
    main()
