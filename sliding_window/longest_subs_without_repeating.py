# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr_chars, left, res = set(), 0, 0
        for right, char in enumerate(s):
            while char in curr_chars:
                curr_chars.discard(s[left])
                left += 1
            curr_chars.add(char)
            res = max(right - left + 1, res)
        return res


class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        positions, left, res = {}, 0, 0
        for right, char in enumerate(s):
            if char in positions and positions[char] >= left:
                left = positions[char] + 1
            positions[char] = right
            res = max(right - left + 1, res)
        return res


def main():
    pass


if __name__ == '__main__':
    main()
