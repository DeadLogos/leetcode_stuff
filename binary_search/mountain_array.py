# https://leetcode.com/problems/peak-index-in-a-mountain-array

class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        left, right = 1, len(arr) - 2
        while left <= right:
            middle = (left + right) // 2
            if arr[middle] > arr[middle + 1] and arr[middle] > arr[middle - 1]:
                return middle
            elif arr[middle] > arr[middle - 1]:
                left = middle + 1
            else:
                right = middle - 1


def main():
    pass


if __name__ == '__main__':
    main()
