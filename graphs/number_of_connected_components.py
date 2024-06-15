# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n))
        self.total_components = n

    def find(self, i):
        if self.parents[i] != i:
            self.parents[i] = self.find(self.parents[i])
        return self.parents[i]

    def join(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parents[root_j] = root_i
            self.total_components -= 1


class Solution:
    def get_total_components(self, n: int, edges: list[list[int]]):
        uf = UnionFind(n)
        for a, b in edges:
            uf.join(a, b)
        return uf.total_components


def main():
    print(Solution().get_total_components(5, [[0, 1], [1, 2], [3, 4]]))


if __name__ == '__main__':
    main()
