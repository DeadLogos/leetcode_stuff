# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/


class Task1:
    class Solution:
        def maxProfit(self, prices: list[int]) -> int:
            curr_min = prices[0]
            res = 0
            for x in prices:
                if x < curr_min:
                    curr_min = x
                else:
                    res = max(x - curr_min, res)
            return res


class Task2:
    class Solution:
        def maxProfit(self, prices: list[int]) -> int:
            curr_min, curr_max = prices[0], None
            res = 0
            for x in prices:
                if curr_max is None:
                    if x > curr_min:
                        curr_max = x
                    else:
                        curr_min = min(curr_min, x)
                elif x < curr_max:
                    res += curr_max - curr_min
                    curr_min, curr_max = x, None
                else:
                    curr_max = max(curr_max, x)
            return res

    class Solution2:
        def maxProfit(self, prices: list[int]) -> int:
            prev_price = prices[0]
            res = 0
            for x in prices:
                if x > prev_price:
                    res += x - prev_price
                prev_price = x
            return res


class Task3:
    class Solution:
        def maxProfit(self, prices: list[int], fee: int) -> int:
            curr_min, curr_max, is_profitable = float('inf'), float('-inf'), False
            res = 0
            for pr in prices:
                if not is_profitable:
                    curr_min, curr_max = (pr, float('-inf')) if pr < curr_min else (curr_min, max(pr, curr_max))
                    is_profitable = curr_max - curr_min > fee
                elif pr > curr_max:
                    curr_max = pr
                elif pr + fee < curr_max:
                    res += curr_max - curr_min - fee
                    curr_min, curr_max, is_profitable = pr, float('-inf'), False
            if is_profitable:
                res += curr_max - curr_min - fee
            return res

    class Solution2:
        def maxProfit(self, prices: list[int], fee: int) -> int:
            hold_profit, free_profit = -prices[0], 0
            for i in range(1, len(prices)):
                price = prices[i]
                hold_profit, free_profit = max(hold_profit, free_profit - price), \
                    max(free_profit, hold_profit + price - fee)
            return free_profit


def main():
    pass


if __name__ == '__main__':
    main()
