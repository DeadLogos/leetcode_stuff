# https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/description/


class Solution:
    def minimizeMax(self, nums: list[int], p: int) -> int:
        nums = sorted(nums)
        diffs = [nums[i] - nums[i - 1] for i in range(1, len(nums))]
        if not diffs:
            return 0

        def helper(max_diff):
            counter = i = 0
            while i < len(diffs):
                if diffs[i] <= max_diff:
                    i += 2
                    counter += 1
                else:
                    i += 1
            return counter >= p

        left, right = -1, max(diffs)
        while left + 1 < right:
            middle = (left + right) // 2
            if helper(middle):
                right = middle
            else:
                left = middle

        return right


def main():
    pass


if __name__ == '__main__':
    main()
