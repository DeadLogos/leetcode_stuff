# https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests/


class Solution:
    def maximumRequests(self, n: int, requests: list[list[int]]) -> int:
        self.res = 0
        change_arr = [0] * n

        def backtrack(i=0, done_reqs=0):
            if i == len(requests):
                if not any(change_arr):
                    self.res = max(self.res, done_reqs)
                return
            change_arr[requests[i][0]] -= 1
            change_arr[requests[i][1]] += 1
            backtrack(i + 1, done_reqs + 1)
            change_arr[requests[i][0]] += 1
            change_arr[requests[i][1]] -= 1
            backtrack(i + 1, done_reqs)

        backtrack()
        return self.res


def main():
    pass


if __name__ == '__main__':
    main()
