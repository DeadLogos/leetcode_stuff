# https://leetcode.com/problems/max-consecutive-ones-iii/


class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = res = curr_zeros = 0
        for right in range(len(nums)):
            if not nums[right] and curr_zeros == k:
                while nums[left]:
                    left += 1
                left += 1
            elif not nums[right]:
                curr_zeros += 1
            res = max(res, right - left + 1)
        return res


class Solution2:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = res = curr_zeros = 0
        for right in range(len(nums)):
            if not nums[right]:
                while curr_zeros == k:
                    if not nums[left]:
                        curr_zeros -= 1
                    left += 1
                curr_zeros += 1
            res = max(res, right - left + 1)
        return res


def main():
    pass


if __name__ == '__main__':
    main()
