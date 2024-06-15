# https://leetcode.com/problems/container-with-most-water/


class Solution:
    def maxArea(self, height: list[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1
        while l < r:
            square = min(height[l], height[r]) * (r - l)
            res = max(res, square)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res


def main():
    pass


if __name__ == '__main__':
    main()
