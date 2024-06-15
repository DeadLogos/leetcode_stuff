# https://leetcode.com/problems/minimum-time-to-make-rope-colorful/


class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        res = 0
        curr_sum, curr_max, curr_color = neededTime[0], neededTime[0], colors[0]
        for i in range(1, len(colors)):
            if colors[i] != curr_color:
                res += curr_sum - curr_max
                curr_sum, curr_max, curr_color = 0, 0, colors[i]
            curr_sum += neededTime[i]
            curr_max = max(neededTime[i], curr_max)
        return res + curr_sum - curr_max


class Solution2:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        res = 0
        curr_max, curr_color = neededTime[0], colors[0]
        for i in range(1, len(colors)):
            if colors[i] != curr_color:
                curr_max, curr_color = neededTime[i], colors[i]
            else:
                res += min(curr_max, neededTime[i])
                curr_max = max(curr_max, neededTime[i])
        return res


def main():
    pass


if __name__ == '__main__':
    main()
