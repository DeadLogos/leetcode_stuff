# https://leetcode.com/problems/arithmetic-subarrays/


class Solution:
    @staticmethod
    def is_arithmetic_subarray_sorting(nums, i, j):
        if i == j:
            return False
        arr = sorted(nums[i:j+1])
        diff = arr[1] - arr[0]
        for k in range(2, len(arr)):
            if arr[k] - arr[k - 1] != diff:
                return False
        return True

    @staticmethod
    def is_arithmetic_subarray_linear(nums, i, j):
        if i == j:
            return False
        subset = set(nums[i:j + 1])
        x, y = min(subset), max(subset)
        if (y - x) % (j - i):
            return False
        diff = (y - x) // (j - i)
        curr = x + diff
        while curr != y:
            if curr not in subset:
                return False
            curr += diff
        return True

    def checkArithmeticSubarrays(self, nums: list[int], l: list[int], r: list[int]) -> list[bool]:
        answer = []
        for i in range(len(l)):
            answer.append(self.is_arithmetic_subarray_linear(nums, l[i], r[i]))
        return answer


def main():
    pass


if __name__ == '__main__':
    main()
