# https://leetcode.com/problems/number-of-good-pairs/

from collections import Counter, defaultdict


class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        counter = Counter(nums)
        res = 0
        for num, freq in counter.items():
            res += sum(range(1, freq))
        return res


class Solution2:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        counter = defaultdict(int)
        res = 0
        for num in nums:
            res += counter[num]
            counter[num] += 1
        return res


def main():
    pass


if __name__ == '__main__':
    main()
