# https://leetcode.com/problems/maximum-subarray/description/


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        curr_sum = 0
        res = float('-inf')
        for x in nums:
            curr_sum += x
            res = max(curr_sum, res)
            if curr_sum < 0:
                curr_sum = 0
        return res if nums else 0


def main():
    pass


if __name__ == '__main__':
    main()
