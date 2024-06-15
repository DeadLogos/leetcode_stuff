# https://leetcode.com/problems/is-subsequence/description/


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        main_pointer, sub_pointer = 0, 0
        while main_pointer < len(t) and sub_pointer < len(s):
            if t[main_pointer] == s[sub_pointer]:
                sub_pointer += 1
            main_pointer += 1
        return sub_pointer == len(s)


def main():
    pass


if __name__ == '__main__':
    main()
