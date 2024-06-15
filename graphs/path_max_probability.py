# https://leetcode.com/problems/path-with-maximum-probability/


from collections import defaultdict
import heapq


class Solution:
    def max_prob(self, n: int, edges: list[list[int]], probs: list[float], start: int, end: int):
        graph = defaultdict(dict)
        for i, (node1, node2) in enumerate(edges):
            graph[node1][node2] = probs[i]
            graph[node2][node1] = probs[i]

        def get_next_node(curr):
            temp_cost, res_node = 0, None
            for i in range(n):
                if not visited[i] and costs[i] > temp_cost:
                    res_node, temp_cost = i, costs[i]
            return res_node

        costs = [0] * n
        costs[start], curr_node = 1, start
        visited = [False] * n
        while curr_node is not None:
            for node, cost in graph[curr_node].items():
                if not visited[node]:
                    new_cost = costs[curr_node] * cost
                    if new_cost > costs[node]:
                        costs[node] = new_cost
            visited[curr_node] = True
            curr_node = get_next_node(curr_node)
        return costs[end]


class Solution2:
    def maxProbability(self, n: int, edges: list[list[int]], probs: list[float], start: int, end: int) -> float:
        graph = defaultdict(dict)
        for i, (node1, node2) in enumerate(edges):
            graph[node1][node2] = probs[i]
            graph[node2][node1] = probs[i]

        costs = [0] * n
        costs[start] = 1
        heap = [(-1.0, start)]
        while heap:
            curr_cost, curr_node = map(abs, heapq.heappop(heap))
            if curr_node == end:
                return -curr_cost
            if curr_cost < costs[curr_node]:
                continue
            for node, cost in graph[curr_node].items():
                new_cost = curr_cost * cost
                if new_cost > costs[node]:
                    costs[node] = new_cost
                    heapq.heappush(heap, (-new_cost, node))
        return costs[end]


def main():
    arr = [[0, 1], [1, 2], [0, 2], [1, 3], [2, 3]]
    prob = [0.2, 0.8, 0.8, 0.5, 0.2]
    print(Solution().max_prob(4, arr, prob, 0, 3))


if __name__ == '__main__':
    main()
