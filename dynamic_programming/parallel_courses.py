# https://leetcode.com/problems/parallel-courses-iii/

from functools import lru_cache


class Solution:
    def minimumTime(self, n: int, relations: list[list[int]], time: list[int]) -> int:
        graph = [set() for _ in range(n)]
        for pr, nxt in relations:
            graph[pr - 1].add(nxt)

        @lru_cache(None)
        def helper(i):
            res = 0
            for node in graph[i]:
                res = max(res, helper(node - 1))
            return res + time[i]

        return max(helper(i) for i in range(n))


def main():
    pass


if __name__ == '__main__':
    main()
