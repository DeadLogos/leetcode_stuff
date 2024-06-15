# https://leetcode.com/problems/longest-common-subsequence/?envType=study-plan-v2&envId=leetcode-75


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2) + 1) for _ in range((len(text1) + 1))]
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                dp[i][j] = (dp[i - 1][j - 1] + 1 if text1[i - 1] == text2[j - 1] else
                            max(dp[i - 1][j], dp[i][j - 1]))
        return dp[-1][-1]


def main():
    pass


if __name__ == '__main__':
    main()
