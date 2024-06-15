# https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

from collections import deque


class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        res = 1
        points = deque([tuple(entrance)])
        used = {tuple(entrance)}

        def is_exit(r, c):
            return not r or not c or r == len(maze) - 1 or c == len(maze[0]) - 1

        # bfs approach
        while points:
            for _ in range(len(points)):
                x, y = points.popleft()
                for i, j in ((x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)):
                    if (i, j) in used or not 0 <= i < len(maze) or not 0 <= j < len(maze[0]) or maze[i][j] == '+':
                        continue
                    if is_exit(i, j):
                        return res
                    points.append((i, j))
                    used.add((i, j))
            res += 1
        return -1


def main():
    arr = [["+", ".", "+", "+", "+", "+", "+"], ["+", ".", "+", ".", ".", ".", "+"],
           ["+", ".", "+", ".", "+", ".", "+"], ["+", ".", ".", ".", "+", ".", "+"],
           ["+", "+", "+", "+", "+", ".", "+"]]
    print(Solution().nearestExit(arr, [0, 1]))


if __name__ == '__main__':
    main()
