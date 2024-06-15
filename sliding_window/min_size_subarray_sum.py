# https://leetcode.com/problems/minimum-size-subarray-sum/


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = right = curr_total = 0
        res = len(nums) + 1
        while right < len(nums) or curr_total >= target:
            print(left, right, curr_total)
            if curr_total < target:
                curr_total += nums[right]
                right += 1
            else:
                curr_total -= nums[left]
                left += 1
            if curr_total >= target:
                res = min(res, right - left)
        return res if res != len(nums) + 1 else 0


class Solution2:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = curr_total = 0
        res = len(nums) + 1
        for right in range(len(nums)):
            curr_total += nums[right]
            while curr_total >= target:
                res = min(res, right - left)
                curr_total -= nums[left]
                left += 1
        return res if res != len(nums) + 1 else 0


def main():
    arr = [2, 3, 1, 2, 4, 3]
    print(Solution().minSubArrayLen(7, arr))


if __name__ == '__main__':
    main()
