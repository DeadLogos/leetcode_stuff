# https://leetcode.com/problems/summary-ranges/description/

class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if not nums:
            return []
        res, j = [], 0
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] > 1:
                res.append(str(nums[j]) if j == i - 1 else f'{nums[j]}->{nums[i - 1]}')
                j = i
        res.append(str(nums[j]) if j == len(nums) - 1 else f'{nums[j]}->{nums[-1]}')
        return res


def main():
    pass


if __name__ == '__main__':
    main()
