# https://leetcode.com/problems/string-compression/


class Solution:
    def compress(self, chars: list[str]) -> int:
        i = end = 0
        while i < len(chars):
            j = i
            while j < len(chars) and chars[i] == chars[j]:
                j += 1
            chars[end] = chars[i]
            end += 1
            if j - i > 1:
                for digit in str(j - i):
                    chars[end] = digit
                    end += 1
            i = j
        chars[end:] = []
        return len(chars)


def main():
    pass


if __name__ == '__main__':
    main()
