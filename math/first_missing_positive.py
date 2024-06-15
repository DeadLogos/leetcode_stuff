# https://leetcode.com/problems/first-missing-positive/description/


# O(n) speed O(n) memory
class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        rng = range(1, len(nums) + 2)
        used = set(filter(lambda x: x in rng, nums))

        for min_pos in rng:
            if min_pos not in used:
                return min_pos


# O(n) speed O(1) memory
class Solution2:
    def firstMissingPositive(self, nums: list[int]) -> int:
        rng = range(1, len(nums) + 1)

        i = 0
        while i < len(nums):
            j = nums[i] - 1
            if nums[i] in rng and nums[i] != i + 1 and nums[j] != nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1


# O(n) speed O(1) memory
class Solution3:
    def firstMissingPositive(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0 or nums[i] > len(nums):
                nums[i] = 0

        for i in range(len(nums)):
            if nums[i]:
                j = abs(nums[i]) - 1
                nums[j] = -abs(nums[j]) or -abs(nums[i])
            print(nums)

        for i in range(len(nums)):
            if nums[i] >= 0:
                return i + 1
        return len(nums) + 1


def main():
    pass


if __name__ == '__main__':
    main()
