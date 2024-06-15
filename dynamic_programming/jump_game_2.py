# https://leetcode.com/problems/jump-game-ii/


# O(n2) dp approach
class Solution:
    def jump(self, nums: list[int]) -> int:
        dp = [len(nums)] * len(nums)
        dp[-1] = 0
        for i in range(len(nums) - 2, -1, -1):
            if nums[i]:
                achievable_spots = range(i + 1, min(len(nums), i + nums[i] + 1))
                dp[i] = dp[min(achievable_spots, key=lambda k: dp[k])] + 1
        return dp[0]


class Solution2:
    def jump(self, nums: list[int]) -> int:
        dp = [len(nums)] * len(nums)
        dp[0] = 0
        for i in range(len(nums)):
            for j in range(i + 1, min(i + nums[i] + 1, len(nums))):
                dp[j] = min(dp[j], dp[i] + 1)
        return dp[-1]


# greedy O(n) approach
class Solution3:
    def jump(self, nums: list[int]) -> int:
        step = left = right = 0
        while right < len(nums) - 1:
            new_right = right + 1
            for i in range(left, right + 1):
                new_right = max(new_right, i + nums[i])
            left, right = right + 1, new_right
            step += 1
        return step


def main():
    pass


if __name__ == '__main__':
    main()
