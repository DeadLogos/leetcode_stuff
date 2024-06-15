# https://leetcode.com/problems/largest-divisible-subset/


class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        nums = sorted(nums)
        dp = [(1, -1)] * len(nums)
        for i in range(1, len(dp)):
            for j in range(i):
                if not (nums[i] % nums[j]) and dp[i][0] < dp[j][0] + 1:
                    dp[i] = (dp[j][0] + 1, j)
        i = dp.index(max(dp, key=lambda x: x[0]))
        res = []
        while i != -1:
            res.append(nums[i])
            i = dp[i][1]
        return res


def main():
    pass


if __name__ == '__main__':
    main()
