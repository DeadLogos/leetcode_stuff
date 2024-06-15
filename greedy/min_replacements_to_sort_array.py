# https://leetcode.com/problems/minimum-replacements-to-sort-the-array/description/


class Solution:
    def minimumReplacement(self, nums: list[int]) -> int:
        res = 0
        prev = float('inf')
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < prev:
                prev = nums[i]
            elif not nums[i] % prev:
                res += nums[i] // prev - 1
            else:
                res += nums[i] // prev
                prev = nums[i] // (nums[i] // prev + 1)
        return res


def main():
    pass


if __name__ == '__main__':
    main()
