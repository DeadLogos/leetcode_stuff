# https://leetcode.com/problems/stone-game/


class Solution:
    def stoneGame(self, piles: list[int]) -> bool:
        dp = {}

        def dfs(l: int, r: int, turn: bool):
            if l > r:
                return 0
            if (l, r) not in dp:
                dp[(l, r)] = max(
                    dfs(l + 1, r, not turn) + (piles[l] if turn else 0),
                    dfs(l, r - 1, not turn) + (piles[r] if turn else 0)
                )
            return dp[(l, r)]

        res = dfs(0, len(piles) - 1, True)
        return res > sum(piles) / 2


# XD
class Solution2:
    def stoneGame(self, piles: list[int]) -> bool:
        return True


def main():
    pass


if __name__ == '__main__':
    main()
