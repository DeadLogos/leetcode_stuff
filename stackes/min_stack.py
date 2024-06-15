# https://leetcode.com/problems/min-stack/


class MinStack:
    def __init__(self):
        self.__stack = []

    def push(self, val: int) -> None:
        new_min = min(val, self.__stack[-1][1] if self.__stack else val)
        self.__stack.append((val, new_min))

    def pop(self) -> None:
        if self.__stack:
            self.__stack.pop()

    def top(self) -> int:
        if self.__stack:
            return self.__stack[-1][0]

    def get_min(self) -> int:
        if self.__stack:
            return self.__stack[-1][1]


def main():
    pass


if __name__ == '__main__':
    main()
