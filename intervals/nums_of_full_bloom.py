# https://leetcode.com/problems/number-of-flowers-in-full-bloom/


class Solution:
    def fullBloomFlowers(self, flowers: list[list[int]], people: list[int]) -> list[int]:
        starts = sorted(map(lambda x: x[0], flowers), reverse=True)
        print(starts)
        ends = sorted(map(lambda x: x[1], flowers), reverse=True)
        print(ends)
        counter, res = 0, [0] * len(people)
        for i, stamp in sorted(enumerate(people), key=lambda x: (x[1], x[0])):
            print(i, stamp)
            while starts and starts[-1] <= stamp:
                counter += 1
                starts.pop()
            while ends and ends[-1] < stamp:
                counter -= 1
                ends.pop()
            res[i] = counter
        return res


def main():
    pass


if __name__ == '__main__':
    main()
