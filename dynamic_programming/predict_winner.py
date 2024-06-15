# https://leetcode.com/problems/predict-the-winner/

from functools import lru_cache


class Solution:
    def PredictTheWinner(self, nums: list[int]) -> bool:
        @lru_cache(None)
        def helper(l, r, score1, score2):
            if l > r:
                return score1 >= score2 if not len(nums) % 2 else score1 > score2
            return not helper(l + 1, r, score2, score1 + nums[l]) or not helper(l, r - 1, score2, score1 + nums[r])

        return helper(0, len(nums) - 1, 0, 0)


class Solution2:
    def PredictTheWinner(self, nums: list[int]) -> bool:
        @lru_cache(None)
        def helper(l, r):
            if l > r:
                return 0
            return max(nums[l] - helper(l + 1, r), nums[r] - helper(l, r - 1))

        return helper(0, len(nums) - 1) >= 0


def main():
    pass


if __name__ == '__main__':
    main()
