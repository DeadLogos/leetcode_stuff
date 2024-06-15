# https://leetcode.com/problems/number-of-provinces/


class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.total = n

    def find(self, elem):
        if self.parents[elem] == elem:
            return elem
        self.parents[elem] = self.find(self.parents[elem])
        return self.parents[elem]

    def join(self, elem1, elem2):
        root1 = self.find(elem1)
        root2 = self.find(elem2)
        if root1 != root2:
            self.parents[root2] = root1
            self.total -= 1


class Solution:
    def find_circle_num(self, is_connected: list[list[int]]) -> int:
        n = len(is_connected)
        uf = UnionFind(n)
        for i in range(n):
            for j in range(i + 1, n):
                if is_connected[i][j]:
                    uf.join(i, j)
        return uf.total


def main():
    pass


if __name__ == '__main__':
    main()
