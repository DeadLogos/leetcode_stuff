# https://leetcode.com/problems/generate-parentheses/

from typing import Optional


class Solution:
    def generateParenthesis(self, n: int, seq: str = '', left: int = 0, right: int = 0,
                            res: Optional[list] = None) -> list[str]:
        if res is None:
            res = []
        if left == right == n:
            res.append(seq)
        else:
            if left < n:
                self.generateParenthesis(n, seq + '(', left + 1, right, res)
            if right < left:
                self.generateParenthesis(n, seq + ')', left, right + 1, res)
        return res


def main():
    pass


if __name__ == '__main__':
    main()
