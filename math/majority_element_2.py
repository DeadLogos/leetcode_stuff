# https://leetcode.com/problems/majority-element-ii/


class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        counter = {}
        for num in nums:
            if num in counter or len(counter) < 2:
                counter[num] = counter.get(num, 0) + 1
            else:
                counter = {x: freq - 1 for x, freq in counter.items() if freq > 1}
        return [x for x in counter if nums.count(x) > len(nums) // 3]


def main():
    pass


if __name__ == '__main__':
    main()
