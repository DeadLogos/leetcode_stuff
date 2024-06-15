# https://leetcode.com/problems/check-if-it-is-a-straight-line/

class Solution:
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
        # y = k * x + b - linear function
        (x1, y1), (x2, y2) = coordinates[:2]
        for x, y in coordinates:
            if (x - x1) * (y2 - y1) != (y - y1) * (x2 - x1):
                return False
        return True


def main():
    print(Solution().checkStraightLine([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]))


if __name__ == '__main__':
    main()
