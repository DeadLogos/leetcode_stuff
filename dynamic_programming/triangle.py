# https://leetcode.com/problems/triangle/description/


class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        dp = [triangle[0][0]]
        for i in range(1, len(triangle)):
            prev = float('inf')
            for j in range(i):
                dp[j], prev = triangle[i][j] + min(prev, dp[j]), dp[j]
            dp.append(prev + triangle[i][-1])
        return min(dp)


def main():
    pass


if __name__ == '__main__':
    main()
