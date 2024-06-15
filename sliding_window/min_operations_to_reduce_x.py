# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/


class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target_sum = sum(nums) - x
        left = curr_sum = 0
        res = -1
        for right in range(len(nums)):
            curr_sum += nums[right]
            while left <= right and curr_sum > target_sum:
                curr_sum -= nums[left]
                left += 1
            if curr_sum == target_sum:
                res = max(res, right - left + 1)
        return len(nums) - res if res != -1 else res


def main():
    pass


if __name__ == '__main__':
    main()
