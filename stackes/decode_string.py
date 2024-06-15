# https://leetcode.com/problems/decode-string/description/


class Solution:
    def decodeString(self, s: str) -> str:

        def helper(s, total=1):
            res = []
            repeat, i = '', 0
            while i < len(s):
                char = s[i]
                if char.isdigit():
                    repeat += char
                elif char == '[':
                    j, stack = i + 1, 1
                    while stack:
                        stack += 1 if s[j] == '[' else -1 if s[j] == ']' else 0
                        j += 1
                    res.append(helper(s[i+1:j-1], int(repeat)))
                    i, repeat = j, ''
                    continue
                else:
                    res.append(char)
                i += 1
            return ''.join(res) * total

        return helper(s)


def main():
    pass


if __name__ == '__main__':
    main()
