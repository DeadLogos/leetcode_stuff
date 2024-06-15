# https://leetcode.com/problems/monotonic-array/


class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        res = False
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                break
        else:
            return True
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                return False
        return True


def main():
    pass


if __name__ == '__main__':
    main()
