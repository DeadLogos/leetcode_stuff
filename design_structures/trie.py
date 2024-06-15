# https://leetcode.com/problems/implement-trie-prefix-tree


class TrieNode:
    def __init__(self):
        self._childes = {}
        self.is_word = False

    @property
    def childes(self):
        return self._childes


class Trie:

    def __init__(self):
        self._root = TrieNode()

    def insert(self, word: str) -> None:
        node = self._root
        for char in word:
            if char not in node.childes:
                node.childes[char] = TrieNode()
            node = node.childes[char]
        node.is_word = True

    def search(self, word: str) -> bool:
        node = self._root
        for char in word:
            if char not in node.childes:
                return False
            node = node.childes[char]
        return node.is_word

    def startsWith(self, prefix: str) -> bool:
        node = self._root
        for char in prefix:
            if char not in node.childes:
                return False
            node = node.childes[char]
        return True


def main():
    pass


if __name__ == '__main__':
    main()
