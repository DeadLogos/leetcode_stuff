# https://leetcode.com/problems/combination-sum-iv

from functools import lru_cache


class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        @lru_cache(None)
        def helper(total):
            if total <= 0:
                return 1 if not total else 0
            res = 0
            for x in nums:
                res += helper(total - x)
            return res

        return helper(target)


class Solution2:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        dp = [1] + [0] * target
        for i in range(1, target + 1):
            for x in nums:
                if i - x >= 0:
                    dp[i] += dp[i - x]
        return dp[-1]


def main():
    pass


if __name__ == '__main__':
    main()
