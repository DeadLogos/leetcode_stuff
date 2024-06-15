# https://leetcode.com/problems/largest-rectangle-in-histogram/


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


def main():
    pass


if __name__ == '__main__':
    main()
