# https://leetcode.com/problems/minimum-window-substring/

from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ''
        res_len = len(s) + 1
        left = 0
        required_chars, required_total = Counter(t), len(t)
        current_chars, current_total = Counter(), 0
        for right, char in enumerate(s):
            if char in required_chars:
                current_chars[char] += 1
                if current_chars[char] <= required_chars[char]:
                    current_total += 1

            while current_total == required_total:
                if right - left + 1 < res_len:
                    res = s[left:right+1]
                    res_len = len(res)
                if s[left] in required_chars:
                    current_chars[s[left]] -= 1
                    if current_chars[s[left]] < required_chars[s[left]]:
                        current_total -= 1
                left += 1
        return res


def main():
    ex = 'ADOBECODBANC'
    print(Solution().minWindow(ex, 'ABC'))


if __name__ == '__main__':
    main()
