# https://leetcode.com/problems/detonate-the-maximum-bombs/

import collections


class Solution:
    def maximumDetonation(self, bombs: list[list[int]]) -> int:
        def is_edge(bomb1, bomb2):
            (x1, y1, r1), (x2, y2, r2) = bomb1, bomb2
            return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5 <= r1

        graph = collections.defaultdict(set)
        for x in range(len(bombs)):
            for y in range(len(bombs)):
                if x != y and is_edge(bombs[x], bombs[y]):
                    graph[x].add(y)

        visited = [False] * len(bombs)

        def bfs(node):
            deq = collections.deque([node])
            used = {node}
            visited[node] = True
            total = 1
            while deq:
                i = deq.popleft()
                for j in graph[i]:
                    if j not in used:
                        deq.append(j)
                        used.add(j)
                        visited[j] = True
                        total += 1
            return total

        res = 1
        for i in range(len(bombs)):
            if not visited[i]:
                res = max(bfs(i), res)
        return res


class Solution2:
    def maximumDetonation(self, bombs: list[list[int]]) -> int:
        def is_edge(bomb1, bomb2):
            (x1, y1, r1), (x2, y2, r2) = bomb1, bomb2
            return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5 <= r1

        def bfs(i):
            deq = collections.deque([i])
            used = {i}
            total = 1
            while deq:
                i = deq.popleft()
                for j in range(len(bombs)):
                    if j != i and j not in used and is_edge(bombs[i], bombs[j]):
                        deq.append(j)
                        used.add(j)
                        total += 1
            return total

        return max(bfs(i) for i in range(len(bombs)))


def main():
    arr = [[54, 95, 4], [99, 46, 3], [29, 21, 3], [96, 72, 8], [49, 43, 3], [11, 20, 3], [2, 57, 1], [69, 51, 7],
           [97, 1, 10], [85, 45, 2], [38, 47, 1], [83, 75, 3], [65, 59, 3], [33, 4, 1], [32, 10, 2], [20, 97, 8],
           [35, 37, 3]]

    arr1 = [[1, 2, 3], [2, 3, 1], [3, 4, 2], [4, 5, 3], [5, 6, 4]]

    ans = Solution().maximumDetonation(arr1)
    print(ans)


if __name__ == '__main__':
    main()
