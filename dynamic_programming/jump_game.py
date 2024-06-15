# https://leetcode.com/problems/jump-game/

from functools import lru_cache


# slow
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        @lru_cache(None)
        def dfs(i: int) -> bool:
            if i >= len(nums) - 1:
                return True
            for j in range(nums[i], 0, -1):
                if dfs(i + j):
                    return True
            return False

        return dfs(0)


class Solution2:
    def canJump(self, nums: list[int]) -> bool:
        last_jumpable = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= last_jumpable:
                last_jumpable = i
        return not last_jumpable


def main():
    pass


if __name__ == '__main__':
    main()
