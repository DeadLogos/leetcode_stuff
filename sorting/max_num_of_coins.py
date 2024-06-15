# https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

from itertools import islice


class Solution:
    def maxCoins(self, piles: list[int]) -> int:
        piles.sort()
        i = len(piles) // 3
        return sum(islice(piles, i, len(piles), 2))


def main():
    pass


if __name__ == '__main__':
    main()
