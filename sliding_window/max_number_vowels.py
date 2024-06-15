# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'
        res = curr = sum(s[i] in vowels for i in range(k))
        for i in range(k, len(s)):
            curr += (s[i] in vowels) - (s[i - k] in vowels)
            res = max(curr, res)
        return res


def main():
    pass


if __name__ == '__main__':
    main()
