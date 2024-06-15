# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

from itertools import product


class Solution:
    mapping = {'2': ('a', 'b', 'c'),
               '3': ('d', 'e', 'f'),
               '4': ('g', 'h', 'i'),
               '5': ('j', 'k', 'l'),
               '6': ('m', 'n', 'o'),
               '7': ('p', 'q', 'r', 's'),
               '8': ('t', 'u', 'v'),
               '9': ('w', 'x', 'y', 'z')
               }

    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        related_letters = [self.mapping[i] for i in digits]
        return list(map(lambda x: ''.join(x), product(*related_letters)))


class Solution2:
    mapping = {'2': ('a', 'b', 'c'),
               '3': ('d', 'e', 'f'),
               '4': ('g', 'h', 'i'),
               '5': ('j', 'k', 'l'),
               '6': ('m', 'n', 'o'),
               '7': ('p', 'q', 'r', 's'),
               '8': ('t', 'u', 'v'),
               '9': ('w', 'x', 'y', 'z')
               }

    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        seq, res = [], []

        def backtrack(i: int):
            if i == len(digits):
                res.append(''.join(seq))
                return
            for char in self.mapping[digits[i]]:
                seq.append(char)
                backtrack(i + 1)
                seq.pop()

        backtrack(0)
        return res


def main():
    pass


if __name__ == '__main__':
    main()
