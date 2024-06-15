# https://leetcode.com/problems/design-hashmap/


from collections import deque


class MyHashMap:
    def __init__(self, *, start_len=10):
        self._arr = [deque() for _ in range(start_len)]
        self._total_pairs = 0

    def _expend_map(self):
        new_arr = [deque() for _ in range(2 * len(self._arr))]
        for deq in self._arr:
            for key, value in deq:
                new_arr[key % len(new_arr)].append((key, value))
        self._arr = new_arr

    def put(self, key: int, value: int) -> None:
        if self._total_pairs == len(self._arr):
            self._expend_map()
        self.remove(key)
        self._arr[key % len(self._arr)].append((key, value))
        self._total_pairs += 1

    def get(self, key: int) -> int:
        for pair in self._arr[key % len(self._arr)]:
            if key == pair[0]:
                return pair[1]
        return -1

    def remove(self, key: int) -> None:
        deq = self._arr[key % len(self._arr)]
        for _ in range(len(deq)):
            pair = deq.popleft()
            if key == pair[0]:
                break
            deq.append(pair)


def main():
    pass


if __name__ == '__main__':
    main()
