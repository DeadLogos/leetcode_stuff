# https://leetcode.com/problems/permutations/description/

from collections import deque


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        self.res = []

        def backtrack(rest_nums):
            if len(rest_nums) == 1:
                return [list(rest_nums)]

            res = []
            for _ in range(len(rest_nums)):
                num = rest_nums.popleft()
                perms = backtrack(rest_nums)

                for arr in backtrack(rest_nums):
                    arr.append(num)
                    res.append(arr)
                rest_nums.append(num)
            return res

        return backtrack(deque(nums))


class Solution2:
    def permute(self, nums: list[int]) -> list[list[int]]:
        self.res = []
        curr_arr = []

        def backtrack(rest_nums):
            if not rest_nums:
                self.res.append(curr_arr.copy())
                return

            for num in rest_nums.copy():
                curr_arr.append(num)
                rest_nums.discard(num)
                backtrack(rest_nums)
                curr_arr.pop()
                rest_nums.add(num)

        backtrack(set(nums))
        return self.res


class Solution3:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res, curr = [], []

        def backtrack():
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            for x in nums:
                if x not in curr:
                    curr.append(x)
                    backtrack()
                    curr.pop()

        backtrack()
        return res


def main():
    pass


if __name__ == '__main__':
    main()
