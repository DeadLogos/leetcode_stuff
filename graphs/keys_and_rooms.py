# https://leetcode.com/problems/keys-and-rooms/


class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        is_opened = [False] * len(rooms)

        def dfs(i):
            if is_opened[i]:
                return
            is_opened[i] = True
            for key in rooms[i]:
                dfs(key)

        dfs(0)
        return all(is_opened)


def main():
    pass


if __name__ == '__main__':
    main()
