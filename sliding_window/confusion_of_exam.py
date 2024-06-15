# https://leetcode.com/problems/maximize-the-confusion-of-an-exam/description/


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        res = left = total = 0
        for right, char in enumerate(answerKey):
            if char == 'T':
                total += 1
                while total > k:
                    total -= answerKey[left] == 'T'
                    left += 1
            res = max(res, right - left + 1)

        left = total = 0
        for right, char in enumerate(answerKey):
            if char == 'F':
                total += 1
                while total > k:
                    total -= answerKey[left] == 'F'
                    left += 1
            res = max(res, right - left + 1)

        return res


class Solution2:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        counter = {'T': 0, 'F': 0}
        res = left = 0
        for right, char in enumerate(answerKey):
            counter[char] += 1
            while min(counter.values()) > k:
                counter[answerKey[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res


class Solution3:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        counter = {'T': 0, 'F': 0}
        res = 0
        for right, char in enumerate(answerKey):
            counter[char] += 1
            if min(counter.values()) > k:
                counter[answerKey[right - res]] -= 1
            else:
                res += 1
        return res


def main():
    pass


if __name__ == '__main__':
    main()
