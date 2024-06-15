# https://leetcode.com/problems/length-of-last-word/description/


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        while s[i] == ' ':
            i -= 1
        length = 0
        while i >= 0 and s[i] != ' ':
            i -= 1
            length += 1
        return length


def main():
    pass


if __name__ == '__main__':
    main()
