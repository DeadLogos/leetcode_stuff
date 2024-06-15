# https://leetcode.com/problems/shortest-path-to-get-all-keys/

from collections import deque


# bfs O(n * m * 2 ** k)
class Solution:
    def shortestPathAllKeys(self, grid: list[str]) -> int:
        total_keys, start = 0, None
        keys, locks = {'a', 'b', 'c', 'd', 'e', 'f'}, {'A', 'B', 'C', 'D', 'E', 'F'}
        for i, row in enumerate(grid):
            for j, char in enumerate(row):
                if char == '@':
                    start = i, j
                elif char in keys:
                    total_keys += 1

        deq = deque([(start, tuple())])
        used, level = {(start, tuple())}, 0
        m, n = len(grid), len(grid[0])
        while deq:
            for _ in range(len(deq)):
                (x, y), curr_keys = deq.popleft()
                if grid[x][y] in keys and grid[x][y] not in curr_keys:
                    curr_keys += (grid[x][y],)
                    if len(curr_keys) == total_keys:
                        return level
                for i, j in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                    point = (x + i, y + j)
                    if 0 <= point[0] < m and 0 <= point[1] < n and (point, curr_keys) not in used:
                        used.add((point, curr_keys))
                        cell = grid[point[0]][point[1]]
                        if cell == '#' or cell in locks and cell.lower() not in curr_keys:
                            continue
                        deq.append((point, curr_keys))
            level += 1
        return -1


def main():
    field = ["#a##", "#.##", "..Ab", "#B.."]
    print(Solution().shortestPathAllKeys(field))


if __name__ == '__main__':
    main()
