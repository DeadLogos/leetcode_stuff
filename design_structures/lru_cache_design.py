# https://leetcode.com/problems/lru-cache/description/


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.lru_node = self.mru_node = None

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        if self.mru_node is node:
            return node.value
        if self.lru_node is node:
            self.lru_node = node.next
        else:
            node.prev.next = node.next
        node.next.prev, node.next = node.prev, None
        self.mru_node.next, node.prev = node, self.mru_node
        self.mru_node = node
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].value = value
            self.get(key)
            return

        new_node = Node(key, value)
        if self.lru_node is None:
            self.lru_node = self.mru_node = new_node
        else:
            self.mru_node.next, new_node.prev = new_node, self.mru_node
            self.mru_node = new_node
        self.cache[key] = new_node

        if len(self.cache) == self.capacity + 1:
            self.cache.pop(self.lru_node.key)
            self.lru_node = self.lru_node.next
            self.lru_node.prev = None


class Node2:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = self.prev = None


class LRUCache2:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.lru_dummy, self.mru_dummy = Node(), Node()
        self.lru_dummy.next, self.mru_dummy.prev = self.mru_dummy, self.lru_dummy

    def update_mru(self, node):
        dummy, last = self.mru_dummy, self.mru_dummy.prev
        last.next, node.prev = node, last
        dummy.prev, node.next = node, dummy

    def remove_node(self, node):
        node.prev.next, node.next.prev = node.next, node.prev

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove_node(node)
        self.update_mru(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].value = value
            self.get(key)
            return

        new_node = Node2(key, value)
        self.update_mru(new_node)
        self.cache[key] = new_node

        if len(self.cache) == self.capacity + 1:
            lru_node = self.lru_dummy.next
            self.cache.pop(lru_node.key)
            self.remove_node(lru_node)


def main():
    pass


if __name__ == '__main__':
    main()
