# https://leetcode.com/problems/max-number-of-k-sum-pairs/

from collections import defaultdict


class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        nums.sort()
        res = 0
        p1, p2 = 0, len(nums) - 1
        while p1 < p2:
            if nums[p1] + nums[p2] == k:
                res += 1
                p1, p2 = p1 + 1, p2 - 1
            elif nums[p1] + nums[p2] < k:
                p1 += 1
            else:
                p2 -= 1
        return res


class Solution2:
    def maxOperations(self, nums: list[int], k: int) -> int:
        met = defaultdict(int)
        res = 0
        for x in nums:
            if not met[k - x]:
                met[x] += 1
            else:
                res += 1
                met[k - x] -= 1
        return res


def main():
    pass


if __name__ == '__main__':
    main()
