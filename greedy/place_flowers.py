# https://leetcode.com/problems/can-place-flowers/


class Solution:
    def canPlaceFlowers(self, fl_bed: list[int], n: int) -> bool:
        possible_total = 0
        i = 0
        while possible_total < n and i < len(fl_bed):
            if fl_bed[i]:
                i += 2
            elif not fl_bed[i] and (not i or not fl_bed[i - 1]) and (i == len(fl_bed) - 1 or not fl_bed[i + 1]):
                possible_total += 1
                i += 2
            else:
                i += 1
        return possible_total == n


class Solution2:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        rest_n, access = n, True
        for i in range(len(flowerbed)):
            if flowerbed[i]:
                access = False
            elif access and (i == len(flowerbed) - 1 or not flowerbed[i + 1]):
                if not rest_n:
                    return True
                rest_n -= 1
                access = False
            else:
                access = True
        return not rest_n


def main():
    pass


if __name__ == '__main__':
    main()
