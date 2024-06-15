# https://leetcode.com/problems/longest-palindromic-substring/description/


class Solution:
    def longestPalindrome(self, s: str) -> str:
        res_left = res_right = 0
        n = len(s)
        for i in range(n):
            left = right = i
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            if right - left - 1 > res_right - res_left:
                res_left, res_right = left + 1, right

            left, right = i, i + 1
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            if right - left - 1 > res_right - res_left:
                res_left, res_right = left + 1, right
        return s[res_left:res_right]


def main():
    pass


if __name__ == '__main__':
    main()
