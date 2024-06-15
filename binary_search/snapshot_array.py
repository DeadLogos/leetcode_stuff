# https://leetcode.com/problems/snapshot-array/


class SnapshotArray:
    def __init__(self, length: int):
        self._arr = [[(0, 0)] for _ in range(length)]
        self._total_snaps = 0

    def set(self, index: int, val: int) -> None:
        if self._arr[index][-1][1] == self._total_snaps:
            self._arr[index].pop()
        self._arr[index].append((val, self._total_snaps))

    def snap(self) -> int:
        self._total_snaps += 1
        return self._total_snaps - 1

    def get(self, index: int, snap_id: int) -> int:
        if snap_id >= self._total_snaps:
            raise IndexError
        search_arr = self._arr[index]
        left, right = -1, len(search_arr)
        while left + 1 < right:
            middle = (left + right) // 2
            if search_arr[middle][1] > snap_id:
                right = middle
            else:
                left = middle
        return search_arr[left][0]


def main():
    obj = SnapshotArray(4)
    obj.set(1, 3)
    obj.set(2, 5)
    obj.snap()
    obj.set(1, 1)
    obj.set(0, 8)
    obj.snap()
    obj.snap()
    obj.set(2, -4)
    obj.snap()
    obj.set(2, 4)

    print(obj.get(2, 3))


if __name__ == '__main__':
    main()
