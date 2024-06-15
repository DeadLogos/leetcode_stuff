# https://leetcode.com/problems/flatten-nested-list-iterator


class NestedInteger:
    def __init__(self, arr):
        self._arr = arr

    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """
        return type(self._arr) == int

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """
        return self._arr

    def getList(self) -> list["NestedInteger"]:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """
        return self._arr


class NestedIterator:
    def __init__(self, nestedList: list[NestedInteger]):
        self._iterator = self._dfs_iterator(nestedList)
        self._curr_next = None

    def _dfs_iterator(self, nested: list[NestedInteger]):
        for ni in nested:
            if ni.isInteger():
                yield ni.getInteger()
            else:
                yield from self._dfs_iterator(ni.getList())

    def next(self) -> int:
        if self.hasNext():
            res = self._curr_next
            self._curr_next = None
            return res

    def hasNext(self) -> bool:
        if self._curr_next is None:
            self._curr_next = next(self._iterator, None)
        return self._curr_next is not None


def main():
    pass


if __name__ == '__main__':
    main()
