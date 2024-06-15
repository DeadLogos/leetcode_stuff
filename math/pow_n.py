# https://leetcode.com/problems/powx-n/


class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if not n:
                return 1
            return helper(x * x, n // 2) * (x if n % 2 else 1)

        res = helper(x, abs(n))
        return res if n >= 0 else 1 / res


def main():
    x, n = int(input()), int(input())
    print(Solution().myPow(x, n))


if __name__ == '__main__':
    main()
