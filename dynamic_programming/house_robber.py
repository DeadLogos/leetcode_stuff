# https://leetcode.com/problems/house-robber/description/?envType=study-plan-v2&envId=top-interview-150


# O(n) memory
class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return max(nums) if nums else 0
        dp = [0] * len(nums)
        dp[0], dp[1], dp[2] = nums[0], nums[1], nums[0] + nums[2]
        for i in range(3, len(nums)):
            dp[i] = max(dp[i - 2], dp[i - 3]) + nums[i]
        return max(dp[-1], dp[-2])


# O(1) memory
class Solution2:
    def rob(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return max(nums) if nums else 0
        prev3, prev2, prev = nums[0], nums[1], nums[0] + nums[2]
        for i in range(3, len(nums)):
            prev3, prev2, prev = prev2, prev, max(prev3, prev2) + nums[i]
        return max(prev, prev2)


# O(1) memory
class Solution3:
    def rob(self, nums: list[int]) -> int:
        left = right = 0
        for cost in nums:
            new_cost = max(right, left + cost)
            left, right = right, new_cost
        return right


def main():
    pass


if __name__ == '__main__':
    main()
