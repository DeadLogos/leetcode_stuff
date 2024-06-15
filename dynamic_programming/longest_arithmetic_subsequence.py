# https://leetcode.com/problems/longest-arithmetic-subsequence/description/


class Solution:
    def longestArithSeqLength(self, nums: list[int]) -> int:
        used_diffs = set()
        max_len = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] - nums[i] not in used_diffs:
                    diff, last, curr_len = nums[j] - nums[i], nums[j], 2
                    for k in range(j + 1, len(nums)):
                        if nums[k] - diff == last:
                            curr_len += 1
                            last = nums[k]
                    max_len = max(max_len, curr_len)
        return max_len


class Solution2:
    def longestArithSeqLength(self, nums: list[int]) -> int:
        dp = {}
        for last in range(1, len(nums)):
            for prev in range(last):
                diff = nums[last] - nums[prev]
                dp[last, diff] = dp.get((prev, diff), 1) + 1
        return max(dp.values())


def main():
    pass


if __name__ == '__main__':
    main()
