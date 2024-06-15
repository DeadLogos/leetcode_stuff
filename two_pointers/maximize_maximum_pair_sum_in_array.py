# https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/


class Solution:
    def minPairSum(self, nums: list[int]) -> int:
        nums.sort()
        i, j = 0, len(nums) - 1
        res = 0
        while i < j:
            res = max(res, nums[i] + nums[j])
            i += 1
            j -= 1
        return res


def main():
    pass


if __name__ == '__main__':
    main()
