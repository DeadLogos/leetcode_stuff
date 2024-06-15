from typing import Hashable
from collections import Counter


class FreqStackObj:
    def __init__(self, data: Hashable):
        self.data = data
        self.next = None
        self.prev = None


class FreqStack:
    def __init__(self):
        self.head = None
        self.tail = None
        self.__freq = Counter()

    def get(self):
        if self.head is None:
            return []
        node = self.head
        res = [node.data]
        while node.next:
            node = node.next
            res.append(node.data)
        return res

    def push(self, x: int) -> None:
        if type(x) != int:
            raise TypeError
        obj = FreqStackObj(x)
        if self.head is None:
            self.head = obj
        else:
            self.tail.next = obj
        obj.prev = self.tail
        self.tail = obj
        self.__freq[obj.data] += 1

    def pop(self):
        if self.head is None:
            raise IndexError('Empty stack')

        most_common = self.__freq.most_common()
        freq_elem, freq_top = most_common[0]
        for i, freq in most_common:
            if freq != freq_top:
                break
            freq_elem = i
        self.__freq[freq_elem] -= 1

        if self.head is self.tail:
            self.head = self.tail = None
        elif self.tail.data == freq_elem:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            node = self.tail
            while node.data != freq_elem:
                node = node.prev
            node.next.prev = node.prev
            node.prev.next = node.next
        return freq_elem


obj = FreqStack()
# Создается пустой стек

obj.push(5)
obj.push(7)
obj.push(5)
obj.push(7)
obj.push(4)
obj.push(5)
print(obj.get())

obj.pop()
print(obj.get())

obj.pop()
print(obj.get())