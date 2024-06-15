# https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

import itertools
from typing import Iterator


class Solution:
    def generator(self, arr: list[str]) -> Iterator[str]:
        for word in arr:
            for char in word:
                yield char

    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        gen1, gen2 = self.generator(word1), self.generator(word2)
        for x, y in itertools.zip_longest(gen1, gen2, fillvalue=None):
            if x != y:
                return False
        return True


def main():
    pass


if __name__ == '__main__':
    main()
