# https://leetcode.com/problems/maximal-network-rank/description/


class Solution:
    def maximalNetworkRank(self, n: int, roads: list[list[int]]) -> int:
        total_roads = [0] * n
        gr = {}
        for i, j in roads:
            total_roads[i] += 1
            total_roads[j] += 1
            gr[(min(i, j), max(i, j))] = True

        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                rank = total_roads[i] + total_roads[j] - (1 if (i, j) in gr else 0)
                res = max(rank, res)
        return res


def main():
    pass


if __name__ == '__main__':
    main()
