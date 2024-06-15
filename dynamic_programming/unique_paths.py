# https://leetcode.com/problems/unique-paths/


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        for _ in range(m - 1):
            for i in range(1, n):
                row[i] = row[i] + row[i - 1]
        return row[-1]


def main():
    pass


if __name__ == '__main__':
    main()
