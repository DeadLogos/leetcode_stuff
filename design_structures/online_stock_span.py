# https://leetcode.com/problems/online-stock-span/


class StockSpanner:
    def __init__(self):
        self._prices = []

    def next(self, price: int) -> int:
        res = 1
        while self._prices and price >= self._prices[-1][0]:
            res += self._prices.pop()[1]
        self._prices.append((price, res))
        return res


def main():
    pass


if __name__ == '__main__':
    main()
