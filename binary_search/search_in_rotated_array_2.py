# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/


class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        l, r = 0, len(nums)
        while l + 1 < r:
            middle = (l + r) // 2
            if nums[middle] > nums[l]:
                l = middle
            elif nums[middle] == nums[l] and not any(nums[i] != nums[middle] for i in range(l, middle)):
                l = middle
            else:
                r = middle

        left, right = (0, l) if target >= nums[0] else (r, len(nums) - 1)
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return True
            elif nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1
        return False


class Solution2:
    def search(self, nums: list[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l <= r:
            middle = (l + r) // 2
            if nums[middle] == target:
                return True
            elif nums[middle] > nums[l]:
                if nums[middle] > target >= nums[l]:
                    r = middle - 1
                else:
                    l = middle + 1
            elif nums[middle] < nums[l]:
                if nums[r] >= target > nums[middle]:
                    l = middle + 1
                else:
                    r = middle - 1
            else:
                l += 1
        return False



def main():
    pass


if __name__ == '__main__':
    main()
