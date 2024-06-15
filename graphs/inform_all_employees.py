# https://leetcode.com/problems/time-needed-to-inform-all-employees/

from collections import defaultdict, deque


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: list[int], informTime: list[int]) -> int:
        graph = defaultdict(set)
        for inferior, superior in enumerate(manager):
            graph[superior].add(inferior)
        deq = deque([(headID, 0)])
        res = 0
        while deq:
            node, curr = deq.popleft()
            if not graph[node]:
                res = max(res, curr)
            else:
                for neighbor in graph[node]:
                    deq.append((neighbor, curr + informTime[node]))
        return res


class Solution2:
    def numOfMinutes(self, n: int, headID: int, manager: list[int], informTime: list[int]) -> int:
        graph = defaultdict(set)
        for inferior, superior in enumerate(manager):
            graph[superior].add(inferior)

        def dfs(node):
            if not graph[node]:
                return 0
            return informTime[node] + max(dfs(neighbor) for neighbor in graph[node])

        return dfs(headID)


def main():
    pass


if __name__ == '__main__':
    main()
