# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/description/


from functools import lru_cache
from bisect import bisect


# backtracking, memory limit exceeded
class Solution0:
    def maxValue(self, events: list[list[int]], k: int) -> int:
        events.sort()
        self.res = 0

        @lru_cache(None)
        def helper(i, value, rest_k):
            if not rest_k or i == len(events):
                self.res = max(value, self.res)
                return

            helper(i + 1, value, rest_k)
            next_i = bisect(events, events[i][1], key=lambda x: x[0])
            helper(next_i, value + events[i][2], rest_k - 1)

        helper(0, 0, k)
        return self.res


class Solution:
    def maxValue(self, events: list[list[int]], k: int) -> int:
        events.sort()
        self.res = 0

        @lru_cache(None)
        def helper(i, rest_k):
            if not rest_k or i == len(events):
                return 0

            not_attending = helper(i + 1, rest_k)
            next_i = bisect(events, events[i][1], key=lambda x: x[0])
            attending = helper(next_i, rest_k - 1) + events[i][2]
            return max(not_attending, attending)

        return helper(0, k)


def main():
    pass


if __name__ == '__main__':
    main()
