# https://leetcode.com/problems/combinations/


class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        self.res = []
        curr_arr = []

        def backtrack(i=1):
            if len(curr_arr) == k:
                self.res.append(curr_arr.copy())
                return

            for j in range(i, n + 1):
                curr_arr.append(j)
                backtrack(j + 1)
                curr_arr.pop()

        backtrack()
        return self.res


def main():
    pass


if __name__ == '__main__':
    main()
