# https://leetcode.com/problems/similar-string-groups/

from collections import defaultdict


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
        self.total = n

    def find(self, elem):
        if self.parent[elem] == elem:
            return elem
        self.parent[elem] = self.find(self.parent[elem])
        return self.parent[elem]

    def join(self, elem1, elem2):
        root1 = self.find(elem1)
        root2 = self.find(elem2)
        if root1 != root2:
            root1, root2 = (root1, root2) if self.size[root1] >= self.size[root2] else (root2, root1)
            self.parent[root2] = root1
            self.size[root1] += self.size[root2]
            self.total -= 1


class Solution:
    @staticmethod
    def is_similar(s1, s2):
        total = 0
        for x, y in zip(s1, s2):
            total += x != y
            if total > 2:
                return False
        return total != 1

    # Решение через Union-Find algorithm
    @classmethod
    def num_similar_groups(cls, strs: list[str]) -> int:
        uf = UnionFind(len(strs))
        for i in range(len(strs)):
            for j in range(i + 1, len(strs)):
                if cls.is_similar(strs[i], strs[j]):
                    uf.join(i, j)
        return uf.total

    # Решение через dfs
    @classmethod
    def num_similar_groups_dfs(cls, strs: list[str]) -> int:
        adjacency_table, n = defaultdict(list), len(strs)
        for i in range(n):
            _ = adjacency_table[i]
            for j in range(i + 1, n):
                if cls.is_similar(strs[i], strs[j]):
                    adjacency_table[i].append(j)
                    adjacency_table[j].append(i)

        def dfs(graph, node, visited):
            if not visited[node]:
                visited[node] = True
                for n_node in graph[node]:
                    dfs(graph, n_node, visited)
            return visited

        res = 0
        treated_nodes = [False] * n
        for i, value in enumerate(treated_nodes):
            if not value:
                res += 1
                dfs(adjacency_table, i, treated_nodes)
        return res


def main():
    print(Solution.num_similar_groups(["tars", "rats", "arts", "star", 'rtsa']))
    print(Solution.num_similar_groups_dfs(["tars", "rats", "arts", "star", 'rtsa']))


if __name__ == '__main__':
    main()
