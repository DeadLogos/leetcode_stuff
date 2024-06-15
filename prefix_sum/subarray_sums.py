# https://leetcode.com/problems/subarray-sum-equals-k/description/

from collections import defaultdict


# brute force
class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            curr_sum = 0
            for j in range(i, len(nums)):
                curr_sum += nums[j]
                if curr_sum == k:
                    res += 1
        return res


# O(n)
class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        prefix_sums, curr_sum = defaultdict(int, {0: 1}), 0
        res = 0
        for x in nums:
            curr_sum += x
            res += prefix_sums.get(curr_sum - k, 0)
            prefix_sums[curr_sum] += 1
        return res


def main():
    pass


if __name__ == '__main__':
    main()
