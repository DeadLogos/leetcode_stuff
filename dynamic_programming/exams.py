# https://leetcode.com/problems/solving-questions-with-brainpower/


class Solution:
    def mostPoints(self, questions: list[list[int]]) -> int:
        cashed = {}

        def find_max_way(i=0):
            if i >= len(questions):
                return 0
            if i not in cashed:
                cashed[i] = max(find_max_way(i + 1), questions[i][0] + find_max_way(i + questions[i][1] + 1))
            return cashed[i]

        return find_max_way()


class Solution:
    def mostPoints(self, questions: list[list[int]]) -> int:
        n = len(questions)
        dp = [0] * n
        for i in range(n - 1, -1, -1):
            score, cost = questions[i]
            dp[i] = max(dp[i + 1] if i + 1 < n else 0, (dp[i + cost + 1] if i + cost + 1 < n else 0) + score)
        return dp[0]


class Solution:
    def mostPoints(self, questions: list[list[int]]) -> int:
        n = len(questions)
        dp = {}
        for i in range(n - 1, -1, -1):
            score, cost = questions[i]
            dp[i] = max(dp.get(i + 1, 0), dp.get(i + cost + 1, 0) + score)
        return dp[0]


def main():
    pass


if __name__ == '__main__':
    main()
