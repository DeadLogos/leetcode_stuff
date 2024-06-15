# https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/


class Solution:
    def garbageCollection(self, garbage: list[str], travel: list[int]) -> int:
        res = 0
        last_G = last_P = last_M = 0
        for i in range(len(garbage) - 1, -1, -1):
            if not last_G and 'G' in garbage[i]:
                last_G = i
            if not last_P and 'P' in garbage[i]:
                last_P = i
            if not last_M and 'M' in garbage[i]:
                last_M = i
            if all((last_G, last_P, last_M)):
                break
        return (sum(map(len, garbage)) + sum(travel[i] for i in range(last_G)) +
                sum(travel[i] for i in range(last_P)) + sum(travel[i] for i in range(last_M)))


def main():
    pass


if __name__ == '__main__':
    main()
