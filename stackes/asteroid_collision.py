# https://leetcode.com/problems/asteroid-collision/description/


class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        res = []
        for asteroid in asteroids:
            if asteroid > 0:
                res.append(asteroid)
            else:
                while res and res[-1] > 0:
                    if res[-1] > abs(asteroid):
                        break
                    last = res.pop()
                    if last == abs(asteroid):
                        break
                else:
                    res.append(asteroid)
        return res


def main():
    pass


if __name__ == '__main__':
    main()
