# https://leetcode.com/problems/regular-expression-matching/


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}

        def inner(i, j):
            if (i, j) in cache:
                return cache[(i, j)]

            if j == len(p):
                return i == len(s)

            res = i < len(s) and (s[i] == p[j] or p[j] == '.')
            if j + 1 < len(p) and p[j + 1] == '*':
                res = inner(i, j + 2) or res and inner(i + 1, j)
            else:
                res = res and inner(i + 1, j + 1)

            cache[(i, j)] = res
            return res

        return inner(0, 0)


def main():
    pass


if __name__ == '__main__':
    main()
