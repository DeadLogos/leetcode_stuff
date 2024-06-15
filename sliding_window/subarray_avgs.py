# https://leetcode.com/problems/k-radius-subarray-averages/


class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        res = [-1] * len(nums)
        window_len = 2 * k + 1

        if window_len > len(nums):
            return res

        curr_total = sum(nums[i] for i in range(window_len))
        res[k] = curr_total // window_len

        for left, right in zip(range(len(nums)), range(window_len, len(nums))):
            curr_total += nums[right] - nums[left]
            res[right - k] = curr_total // window_len

        return res


def main():
    pass


if __name__ == '__main__':
    main()
