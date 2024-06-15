# https://leetcode.com/problems/trapping-rain-water/


class Solution:
    def trap(self, height: list[int]) -> int:
        next_max = [0] * len(height)
        curr_max = 0
        for i in range(len(height) - 1, -1, -1):
            next_max[i] = curr_max
            curr_max = max(curr_max, height[i])

        prev_max = res = 0
        for i in range(len(height)):
            trapped_water = min(prev_max, next_max[i]) - height[i]
            if trapped_water > 0:
                res += trapped_water
            prev_max = max(prev_max, height[i])
        return res


class Solution2:
    def trap(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        res = 0
        while left + 1 < right:
            if left_max <= right_max:
                left += 1
                left_max = max(left_max, height[left])
                res += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                res += right_max - height[right]
        return res


def main():
    arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(Solution2().trap(arr))


if __name__ == '__main__':
    main()
