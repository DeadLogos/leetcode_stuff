# https://leetcode.com/problems/is-graph-bipartite/

from collections import deque
from typing import List


class Solution:
    def get_all_groups(self, graph):
        class UnionFind:
            def __init__(self, n):
                self.parents = list(range(n))
                self.pointers = set(range(n))

            def find(self, elem):
                if self.parents[elem] == elem:
                    return elem
                self.parents[elem] = self.find(self.parents[elem])
                return self.parents[elem]

            def union(self, elem1, elem2):
                root1 = self.find(elem1)
                root2 = self.find(elem2)
                if root1 != root2:
                    self.parents[root2] = root1
                    self.pointers.discard(root2)

        uf = UnionFind(len(graph))
        for i, x in enumerate(graph):
            for j in x:
                if j > i:
                    uf.union(i, j)
        return uf.pointers

    def is_bipartite(self, graph: List[List[int]]) -> bool:
        def dfs(i: int, level: int, used: dict):
            if i in used and (level - used[i]) % 2:
                return False
            elif i not in used:
                used[i] = level
                for node in graph[i]:
                    if not dfs(node, level + 1, used):
                        return False
            return True

        for group in self.get_all_groups(graph):
            if not dfs(group, 0, {}):
                return False
        return True


class Solution2:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        used = [0] * len(graph)

        def bfs(i):
            deq = deque([i])
            used[i] = 1
            while deq:
                node = deq.popleft()
                for adj in graph[node]:
                    if used[adj] == used[node]:
                        return False
                    elif not used[adj]:
                        used[adj] = used[node] * -1
                        deq.append(adj)
            return True

        for x in range(len(graph)):
            if not used[x] and not bfs(x):
                return False
        return True


def main():
    pass


if __name__ == '__main__':
    main()
