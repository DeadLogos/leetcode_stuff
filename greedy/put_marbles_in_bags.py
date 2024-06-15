# https://leetcode.com/problems/put-marbles-in-bags/description/


class Solution:
    def putMarbles(self, weights: list[int], k: int) -> int:
        if k == 1:
            return 0
        edge_points = sorted(weights[i] + weights[i - 1] for i in range(1, len(weights)))
        max_score = sum(edge_points[-k + 1:]) + weights[0] + weights[-1]
        min_score = sum(edge_points[:k - 1]) + weights[0] + weights[-1]
        return max_score - min_score


def main():
    pass


if __name__ == '__main__':
    main()
