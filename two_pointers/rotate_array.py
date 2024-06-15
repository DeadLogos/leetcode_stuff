# https://leetcode.com/problems/rotate-array/


class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        k %= len(nums)
        left, right = 0, len(nums) - k
        while right - left and len(nums) - right:
            temp = right
            for _ in range(min(right - left, len(nums) - right)):
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right += 1
            right = right if left == temp else temp


class Solution2:
    def rotate(self, nums: list[int], k: int) -> None:
        k %= len(nums)
        nums.reverse()

        l, r = 0, k - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        l, r = k, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1


def main():
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    print(Solution().rotate(arr, 5))


if __name__ == '__main__':
    main()
