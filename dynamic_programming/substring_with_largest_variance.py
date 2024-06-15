# https://leetcode.com/problems/substring-with-largest-variance/description/

from collections import Counter
from itertools import product


class Solution:
    def largestVariance(self, s: str) -> int:
        counter = Counter(s)
        res = 0
        for major, minor in product(counter, counter):
            if major == minor:
                continue
            major_count = minor_count = 0
            rest_minor = counter[minor]
            for char in s:
                if char == major:
                    major_count += 1
                elif char == minor:
                    minor_count += 1
                    rest_minor -= 1
                    if minor_count > major_count and rest_minor > 0:
                        minor_count = major_count = 0
                if minor_count > 0:
                    res = max(major_count - minor_count, res)
        return res


def main():
    pass


if __name__ == '__main__':
    main()
