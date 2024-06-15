# https://leetcode.com/problems/remove-duplicate-letters/

from collections import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        freq, used = Counter(s), dict.fromkeys(set(s), False)
        res = []
        for char in s:
            if used[char]:
                freq[char] -= 1
                continue
            while res and res[-1] >= char and freq[res[-1]]:
                used[res.pop()] = False
            res.append(char)
            freq[char] -= 1
            used[char] = True
        return ''.join(res)


def main():
    pass


if __name__ == '__main__':
    main()
