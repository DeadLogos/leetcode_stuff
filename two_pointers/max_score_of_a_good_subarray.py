# https://leetcode.com/problems/maximum-score-of-a-good-subarray/


class Solution:
    def maximumScore(self, nums: list[int], k: int) -> int:
        i = j = k
        curr_min = nums[k]
        res = curr_min * (j - i + 1)
        while i > 0 or j < len(nums) - 1:
            if j == len(nums) - 1 or (i > 0 and nums[i - 1] > nums[j + 1]):
                i -= 1
                curr_min = min(nums[i], curr_min)
            else:
                j += 1
                curr_min = min(nums[j], curr_min)
            res = max(res, curr_min * (j - i + 1))
        return res


def main():
    pass


if __name__ == '__main__':
    main()
