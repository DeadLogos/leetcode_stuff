# https://leetcode.com/problems/total-cost-to-hire-k-workers/description/

import heapq


class Solution:
    def totalCost(self, costs: list[int], k: int, candidates: int) -> int:
        left, right = candidates, len(costs) - candidates
        heap, res = [], 0
        for i, cost in enumerate(costs):
            if i < left or i >= right:
                heapq.heappush(heap, (cost, i))
        for _ in range(k):
            cost, i = heapq.heappop(heap)
            if left >= right:
                pass
            elif i < left:
                heapq.heappush(heap, (costs[left], left))
                left += 1
            else:
                right -= 1
                heapq.heappush(heap, (costs[right], right))
            res += cost
        return res


def main():
    pass


if __name__ == '__main__':
    main()
