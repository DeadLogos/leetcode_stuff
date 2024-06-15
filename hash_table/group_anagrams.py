# https://leetcode.com/problems/group-anagrams/

from collections import defaultdict
from string import ascii_lowercase


class Solution:
    @staticmethod
    def _produce_key(s: str) -> str:
        letters_totals = dict.fromkeys(ascii_lowercase, 0)
        for char in s:
            letters_totals[char] += 1
        return ''.join([key * value for key, value in letters_totals.items() if value])

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups_anagrams = defaultdict(list)
        for s in strs:
            groups_anagrams[self._produce_key(s)].append(s)
        return list(groups_anagrams.values())


class Solution2:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups_anagrams = defaultdict(list)
        for s in strs:
            groups_anagrams[''.join(sorted(s))].append(s)
        return list(groups_anagrams.values())


class Solution3:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups_anagrams = defaultdict(list)
        for s in strs:
            counting_arr = [0] * 26
            for char in s:
                counting_arr[ord(char) - ord('a')] += 1
            groups_anagrams[tuple(counting_arr)].append(s)
        return list(groups_anagrams.values())


def main():
    pass


if __name__ == '__main__':
    main()
