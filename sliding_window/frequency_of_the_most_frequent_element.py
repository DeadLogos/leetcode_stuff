# https://leetcode.com/problems/frequency-of-the-most-frequent-element/


class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        nums.sort()
        i = curr_cost = 0
        res = 1
        for j in range(1, len(nums)):
            curr_cost += (j - i) * (nums[j] - nums[j - 1])
            while curr_cost > k:
                curr_cost -= nums[j] - nums[i]
                i += 1
            res = max(res, j - i + 1)
        return res


def main():
    pass


if __name__ == '__main__':
    main()
