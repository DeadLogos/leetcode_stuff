# https://leetcode.com/problems/determine-if-two-strings-are-close/

from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1, c2 = Counter(word1), Counter(word2)
        if c1.total() != c2.total() or c1.keys() != c2.keys():
            return False
        return sorted(c1.values()) == sorted(c2.values())


def main():
    pass


if __name__ == '__main__':
    main()
