# https://leetcode.com/problems/maximal-rectangle/


class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        res = 0
        for i, h in enumerate(heights):
            j = i
            while stack and stack[-1][0] > h:
                h_pop, i_pop = stack.pop()
                res = max(res, (i - i_pop) * h_pop)
                j = i_pop
            stack.append((h, j))
        while stack:
            h, i = stack.pop()
            res = max(res, (len(heights) - i) * h)
        return res

    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        res = 0
        dp = [0] * n
        for row in matrix:
            for i, x in enumerate(row):
                dp[i] = 0 if x == '0' else dp[i] + 1
            res = max(res, self.largestRectangleArea(dp))
        return res


def main():
    pass


if __name__ == '__main__':
    main()
