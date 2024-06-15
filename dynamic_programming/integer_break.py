# https://leetcode.com/problems/integer-break/

from functools import lru_cache


class Solution:
    def integerBreak(self, n: int) -> int:
        prev_prod = 0
        for k in range(2, n + 1):
            div, mod = divmod(n, k)
            curr_prod = div ** (k - mod) * (div + 1) ** mod
            if curr_prod < prev_prod:
                return prev_prod
            prev_prod = curr_prod
        return prev_prod


class Solution2:
    def integerBreak(self, n: int) -> int:
        @lru_cache(None)
        def helper(x):
            if x == 1:
                return 1
            res = x if x != n else 1
            for i in range(1, x):
                res = max(res, helper(i) * helper(x - i))
            return res

        return helper(n)


class Solution3:
    def integerBreak(self, n: int) -> int:
        dp = [i for i in range(n)] + [1]
        for i in range(2, n + 1):
            l, r = 1, i - 1
            while l <= r:
                dp[i] = max(dp[l] * dp[r], dp[i])
                l += 1
                r -= 1
        return dp[n]


def main():
    pass


if __name__ == '__main__':
    main()
