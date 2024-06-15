# https://leetcode.com/problems/majority-element/


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        res, counter = None, 0
        for x in nums:
            if x == res:
                counter += 1
            elif not counter:
                res, counter = x, 1
            else:
                counter -= 1
        return res


def main():
    pass


if __name__ == '__main__':
    main()
