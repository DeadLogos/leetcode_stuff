# https://leetcode.com/problems/find-pivot-index


# space 0(n)
class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        prefix_sum = []
        curr_sum = 0
        for x in nums:
            curr_sum += x
            prefix_sum.append(curr_sum)
        for i in range(len(nums)):
            if (prefix_sum[i - 1] if i else 0) == prefix_sum[-1] - prefix_sum[i]:
                return i
        return -1


# space 0(1)
class Solution2:
    def pivotIndex(self, nums: list[int]) -> int:
        nums_sum = sum(nums)
        curr_sum = 0
        for i, x in enumerate(nums):
            if curr_sum == nums_sum - curr_sum - x:
                return i
            curr_sum += x
        return -1


def main():
    pass


if __name__ == '__main__':
    main()
