# https://leetcode.com/problems/binary-trees-with-factors/

from functools import lru_cache


class Solution:
    def numFactoredBinaryTrees(self, arr: list[int]) -> int:
        nums = sorted(arr)
        set_nums = dict(map(reversed, enumerate(nums)))

        @lru_cache(None)
        def helper(i):
            res = 1
            for j in range(i - 1, -1, -1):
                if not nums[i] % nums[j] and nums[i] // nums[j] in set_nums:
                    res += helper(j) * helper(set_nums[nums[i] // nums[j]])
            return res

        return sum(helper(i) for i in range(len(nums) - 1, -1, -1)) % (10 ** 9 + 7)


def main():
    pass


if __name__ == '__main__':
    main()
