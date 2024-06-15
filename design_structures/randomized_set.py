# https://leetcode.com/problems/insert-delete-getrandom-o1/

from random import randint


class RandomizedSet:
    def __init__(self):
        self._arr = []
        self._indexes = {}

    def insert(self, val: int) -> bool:
        if val in self._indexes:
            return False
        self._indexes[val] = len(self._arr)
        self._arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self._indexes:
            return False
        rm_index = self._indexes[val]
        self._indexes[self._arr[-1]] = rm_index
        self._arr[rm_index] = self._arr[-1]
        self._indexes.pop(val)
        self._arr.pop()
        return True

    def getRandom(self) -> int:
        rnd_index = randint(0, len(self._arr) - 1)
        return self._arr[rnd_index]


def main():
    pass


if __name__ == '__main__':
    main()
