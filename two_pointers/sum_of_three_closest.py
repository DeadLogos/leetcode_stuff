# https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, len(nums) - 1
            while j < k:
                curr_sum = nums[j] + nums[k] + nums[i]
                if not curr_sum:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                elif curr_sum < 0:
                    j += 1
                else:
                    k -= 1
        return res


class Solution2:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        def two_sum(i):
            seen = set()
            target = -nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j] in seen:
                    yield target - nums[j], nums[j]
                else:
                    seen.add(target - nums[j])

        res = set()
        used = set()
        for i in range(len(nums) - 2):
            first = nums[i]
            if first in used:
                continue
            for second, third in two_sum(i):
                res.add(tuple(sorted([first, second, third])))
            used.add(first)

        return res


def main():
    pass


if __name__ == '__main__':
    main()
