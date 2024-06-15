# https://leetcode.com/problems/tallest-billboard/description/


class Solution:
    def tallestBillboard(self, rods: list[int]) -> int:
        dp = {0: 0}
        for x in rods:
            new_dp = dp.copy()
            for diff, shorter in dp.items():
                taller = shorter + diff
                new_diff = taller + x - shorter
                new_dp[new_diff] = max(new_dp.get(new_diff, 0), shorter)
                new_diff = abs(shorter + x - taller)
                new_dp[new_diff] = max(new_dp.get(new_diff, 0), min(taller, shorter + x))
            dp = new_dp
        return dp[0]


def main():
    print(Solution().tallestBillboard([2, 3, 1, 1]))


if __name__ == '__main__':
    main()
