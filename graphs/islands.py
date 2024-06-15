# https://leetcode.com/problems/number-of-islands/


class Solution:
    @staticmethod
    def define_island(i, j, grid):
        grid[i][j] = -1

        def fill(x, y):
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and (x > i or x == i and y >= j) and grid[x][y] == 1:
                grid[x][y] = -1
                return True
            return False

        points = [(i, j)]
        while points:
            temp = []
            for point in points:
                for i_inc, j_inc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    if fill(point[0] + i_inc, point[1] + j_inc):
                        temp.append((point[0] + i_inc, point[1] + j_inc))
            points = temp.copy()
            temp.clear()

    def dfs(self, i, j, grid):
        if not 0 <= i < len(grid) or not 0 <= j < len(grid[0]) or grid[i][j] == 0:
            return
        grid[i][j] = 0
        for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            self.dfs(i + x, j + y, grid)

    def num_islands(self, grid: list[list[int | str]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.dfs(i, j, grid)
                    res += 1
        return res


def main():
    arr = [["1", "1", "1", "1", "1", "0", "1", "1", "1", "1"], ["1", "0", "1", "0", "1", "1", "1", "1", "1", "1"],
           ["0", "1", "1", "1", "0", "1", "1", "1", "1", "1"], ["1", "1", "0", "1", "1", "0", "0", "0", "0", "1"],
           ["1", "0", "1", "0", "1", "0", "0", "1", "0", "1"], ["1", "0", "0", "1", "1", "1", "0", "1", "0", "0"],
           ["0", "0", "1", "0", "0", "1", "1", "1", "1", "0"], ["1", "0", "1", "1", "1", "0", "0", "1", "1", "1"],
           ["1", "1", "1", "1", "1", "1", "1", "1", "0", "1"], ["1", "0", "1", "1", "1", "1", "1", "1", "1", "0"]]
    arr = [[int(e) for e in row] for row in arr]
    sol = Solution()
    print(sol.num_islands(arr))


if __name__ == '__main__':
    main()
