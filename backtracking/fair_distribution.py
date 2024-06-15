# https://leetcode.com/problems/fair-distribution-of-cookies/


class Solution:
    def distributeCookies(self, cookies: list[int], k: int) -> int:
        self.res = float('inf')
        distribute_arr = [0] * k

        def backtrack(i, total_deprived):
            if len(cookies) - i < total_deprived:
                return
            if i == len(cookies):
                self.res = min(max(distribute_arr), self.res)
                return

            for j in range(k):
                distribute_arr[j] += cookies[i]
                backtrack(i + 1, total_deprived - (1 if distribute_arr[j] == cookies[i] else 0))
                distribute_arr[j] -= cookies[i]

        backtrack(0, k)
        return self.res


def main():
    pass


if __name__ == '__main__':
    main()
