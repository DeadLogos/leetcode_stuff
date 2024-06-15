# https://leetcode.com/problems/sort-vowels-in-a-string/

from collections import defaultdict


class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        counter = defaultdict(int)
        for char in s:
            if char in vowels:
                counter[char] += 1
        ordered_vowels_gen = (char for char in sorted(vowels) for _ in range(counter[char]))
        res = []
        for char in s:
            res.append(char if char not in vowels else next(ordered_vowels_gen))
        return ''.join(res)


def main():
    pass


if __name__ == '__main__':
    main()
