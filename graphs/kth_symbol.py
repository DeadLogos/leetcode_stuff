# https://leetcode.com/problems/k-th-symbol-in-grammar/


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def helper(i):
            if i <= 1:
                return i
            prev = helper(i // 2)
            return int(prev and not i % 2 or not prev and i % 2)

        return helper(k - 1)


def main():
    pass


if __name__ == '__main__':
    main()
