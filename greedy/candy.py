# https://leetcode.com/problems/candy/


class Solution:
    def candy(self, ratings: list[int]) -> int:
        distributes = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                distributes[i] = distributes[i - 1] + 1
            else:
                distributes[i - 1] = 0

        for i in range(len(ratings) - 2, -1, -1):
            if not distributes[i]:
                distributes[i] = max(distributes[i + 1] + 1 if ratings[i] != ratings[i + 1] else 1, 1)
            elif distributes[i + 1] <= distributes[i]:
                distributes[i + 1] = distributes[i] + 1
        return sum(distributes)


class Solution2:
    def candy(self, ratings: list[int]) -> int:
        distributes = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                distributes[i] = distributes[i - 1] + 1

        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and distributes[i] <= distributes[i + 1]:
                distributes[i] = distributes[i + 1] + 1
        return sum(distributes)


def main():
    pass


if __name__ == '__main__':
    main()
