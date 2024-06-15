# https://leetcode.com/problems/painting-the-walls/


class Solution:
    def paintWalls(self, cost: list[int], time: list[int]) -> int:
        def helper(i, rest):
            if rest == 0:
                return 0

            return min(helper(i + 1, rest - 1),
                       helper(i + 1, rest - 1 - time[i]) + cost[i])


def main():
    pass


if __name__ == '__main__':
    main()
