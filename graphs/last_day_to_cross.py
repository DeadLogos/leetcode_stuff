# https://leetcode.com/problems/last-day-where-you-can-still-cross/description/

from collections import deque


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: list[list[int]]) -> int:
        def helper(k):
            grid = [[0] * col for _ in range(row)]
            for i, j in cells[:k + 1]:
                grid[i - 1][j - 1] = 1

            deq = deque([(0, j) for j in range(col) if not grid[0][j]])
            while deq:
                cell = deq.popleft()
                if cell[0] == row - 1:
                    return True
                for x, y in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                    point = cell[0] + x, cell[1] + y
                    if 0 <= point[0] < row and 0 <= point[1] < col and not grid[point[0]][point[1]]:
                        grid[point[0]][point[1]] = -1
                        deq.append(point)
            return False

        left, right = 0, row * col - 1
        while left + 1 != right:
            middle = (left + right) // 2
            print(left, right, middle)
            h = helper(middle)
            print(h)
            if h:
                left = middle
            else:
                right = middle
        return left + 1


class Solution2:
    class UnionFind:
        def __init__(self, n):
            self.parent = list(range(n))

        def find(self, elem):
            if self.parent[elem] != elem:
                self.parent[elem] = self.find(self.parent[elem])
            return self.parent[elem]

        def join(self, elem1, elem2):
            root1, root2 = self.find(elem1), self.find(elem2)
            if root1 != root2:
                self.parent[root2] = root1

    def latestDayToCross(self, row: int, col: int, cells: list[list[int]]) -> int:
        uf = self.__class__.UnionFind(row * col + 2)
        lands = set()

        for i in range(len(cells) - 1, -1, -1):
            x, y = cells[i][0] - 1, cells[i][1] - 1
            lands.add((x, y))
            for shift_x, shift_y in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                new_x, new_y = x + shift_x, y + shift_y
                if 0 <= new_x < row and 0 <= new_y < col and (new_x, new_y) in lands:
                    uf.join(x * col + y, new_x * col + new_y)

            if x == 0:
                uf.join(x * col + y, row * col)
            elif x == row - 1:
                uf.join(x * col + y, row * col + 1)
            if uf.find(row * col) == uf.find(row * col + 1):
                return i


def main():
    arr = [[1, 2], [2, 1], [3, 3], [2, 2], [1, 1], [1, 3], [2, 3], [3, 2], [3, 1]]
    row, col = 3, 3
    print(Solution2().latestDayToCross(row, col, arr))


if __name__ == '__main__':
    main()
