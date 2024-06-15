# https://leetcode.com/problems/ransom-note/

from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rest = Counter(magazine)
        for char in ransomNote:
            rest[char] -= 1
            if rest[char] < 0:
                return False
        return True


def main():
    pass


if __name__ == '__main__':
    main()
