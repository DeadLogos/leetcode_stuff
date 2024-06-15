# https://leetcode.com/problems/combination-sum-iii/


class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        res = []
        curr_comb = []

        def backtrack(rest_k, rest_n, last_number=0):
            if not rest_k and not rest_n:
                res.append(curr_comb.copy())
                return
            if not rest_k or rest_n > n:
                return
            for number in range(last_number + 1, 10):
                curr_comb.append(number)
                backtrack(rest_k - 1, rest_n - number, number)
                curr_comb.pop()

        backtrack(k, n)
        return res


def main():
    pass


if __name__ == '__main__':
    main()
