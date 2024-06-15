# https://leetcode.com/problems/count-all-possible-routes/description/

from functools import lru_cache


class Solution:
    def countRoutes(self, locations: list[int], start: int, finish: int, fuel: int) -> int:
        @lru_cache(None)
        def helper(point, rest_fuel):
            if abs(locations[finish] - locations[point]) > rest_fuel:
                return 0
            res = 0
            if point == finish:
                res += 1
            for i in range(len(locations)):
                if i != point:
                    res += helper(i, rest_fuel - abs(locations[i] - locations[point]))
            return res

        return helper(start, fuel) % (10**9 + 7)


class Solution2:
    def countRoutes(self, locations: list[int], start: int, finish: int, fuel: int) -> int:
        dp = [[0 if i != finish else 1] * (fuel + 1) for i in range(len(locations))]
        for j in range(1, fuel + 1):
            for i in range(len(locations)):
                for k in range(len(locations)):
                    if k != i:
                        if j >= abs(locations[i] - locations[k]):
                            dp[i][j] += dp[k][j - abs(locations[i] - locations[k])]
        return dp[start][-1]


def main():
    pass


if __name__ == '__main__':
    main()
