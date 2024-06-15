# https://leetcode.com/problems/coin-change/


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for x in coins:
                if i - x >= 0:
                    dp[i] = min(dp[i], dp[i - x] + 1)
        return dp[-1] if dp[-1] != float('inf') else -1


class Solution2:
    def coinChange(self, coins: list[int], amount: int) -> int:
        cache = {}

        def helper(rest_amount: int):
            if rest_amount == 0:
                return 0
            if rest_amount not in cache:
                local_min = float('inf')
                for i in range(len(coins)):
                    if rest_amount - coins[i] >= 0:
                        local_min = min(local_min, helper(rest_amount - coins[i]) + 1)
                cache[rest_amount] = local_min
            return cache[rest_amount]

        res = helper(amount)
        return res if res != float('inf') else -1


def main():
    pass


if __name__ == '__main__':
    main()
