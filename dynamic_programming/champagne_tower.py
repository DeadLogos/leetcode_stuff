# https://leetcode.com/problems/champagne-tower


class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        glasses = [poured]
        for i in range(1, query_row + 1):
            next_row = [0] * (i + 1)
            for j in range(i):
                if glasses[j] <= 1:
                    continue
                next_row[j] += (glasses[j] - 1) / 2
                next_row[j + 1] += (glasses[j] - 1) / 2
            glasses = next_row
        return min(1.0, glasses[query_glass])


def main():
    pass


if __name__ == '__main__':
    main()
