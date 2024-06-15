# https://leetcode.com/problems/number-of-longest-increasing-subsequence/description/


class Solution:
    def findNumberOfLIS(self, nums: list[int]) -> int:
        longest = 1
        dp = [(1, 1)] * len(nums)
        for i in range(len(nums)):
            for j in range(i - 1, -1, -1):
                if nums[i] > nums[j]:
                    if dp[j][0] >= dp[i][0]:
                        dp[i] = (dp[j][0] + 1, dp[j][1])
                    elif dp[j][0] + 1 == dp[i][0]:
                        dp[i] = (dp[i][0], dp[i][1] + dp[j][1])
            longest = max(longest, dp[i][0])
        return sum(map(lambda x: x[1] if x[0] == longest else 0, dp))


class Solution2:
    def findNumberOfLIS(self, nums: list[int]) -> int:
        longest = 1
        dp_length = [1] * len(nums)
        dp_total = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i - 1, -1, -1):
                if nums[i] > nums[j]:
                    if dp_length[j] >= dp_length[i]:
                        dp_length[i] = dp_length[j] + 1
                        dp_total[i] = dp_total[j]
                    elif dp_length[j] + 1 == dp_length[i]:
                        dp_total[i] += dp_total[j]
            longest = max(longest, dp_length[i])
        return sum(map(lambda x: x[1] if x[0] == longest else 0, zip(dp_length, dp_total)))


def main():
    pass


if __name__ == '__main__':
    main()
