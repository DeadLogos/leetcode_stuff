# https://leetcode.com/problems/word-break/

from collections import deque
from functools import lru_cache


# bfs
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        set_words = set(wordDict)
        deq = deque([0])
        used = set()

        while deq:
            i = deq.popleft()
            if i == len(s):
                return True

            for j in range(i + 1, len(s) + 1):
                if j not in used and s[i:j] in set_words:
                    deq.append(j)
                    used.add(j)

        return False


# dp top-down
class Solution2:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        @lru_cache(None)
        def helper(i):
            if i >= len(s):
                return i == len(s)

            for word in wordDict:
                if s[i:i + len(word)] == word and helper(i + len(word)):
                    return True

            return False

        return helper(0)


# dp bottom-up
class Solution3:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(len(s)):
            for word in wordDict:
                if len(word) - 1 > i:
                    continue
                if dp[i + 1 - len(word)] and s[i - len(word) + 1:i + 1] == word:
                    dp[i + 1] = True
                    break
        return dp[-1]


def main():
    pass


if __name__ == '__main__':
    main()
