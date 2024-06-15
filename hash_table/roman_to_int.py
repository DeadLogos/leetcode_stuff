# https://leetcode.com/problems/roman-to-integer/description/


class Solution:
    def romanToInt(self, s: str) -> int:
        matches = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        res = last = 0
        for char in s:
            res += matches[char]
            if matches[char] > last:
                res -= 2 * last
            last = matches[char]
        return res


def main():
    pass


if __name__ == '__main__':
    main()
