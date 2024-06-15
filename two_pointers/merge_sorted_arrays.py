# https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        for i in range(m - 1, -1, -1):
            nums1[i + n] = nums1[i]

        pointer1, pointer2, curr = n, 0, 0

        while pointer1 < n + m and pointer2 < n:
            if nums1[pointer1] < nums2[pointer2]:
                nums1[curr] = nums1[pointer1]
                pointer1 += 1
            else:
                nums1[curr] = nums2[pointer2]
                pointer2 += 1
            curr += 1

        if pointer1 == n + m:
            for i, j in zip(range(pointer2, n), range(curr, n + m)):
                nums1[j] = nums2[i]


class Solution2:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        pointer1, pointer2, curr = m - 1, n - 1, n + m - 1

        while pointer1 >= 0 and pointer2 >= 0:
            if nums1[pointer1] > nums2[pointer2]:
                nums1[curr] = nums1[pointer1]
                pointer1 -= 1
            else:
                nums1[curr] = nums2[pointer2]
                pointer2 -= 1
            curr -= 1

        if pointer1 < 0:
            for i, j in zip(range(pointer2, -1, -1), range(curr, -1, -1)):
                nums1[j] = nums2[i]


class Solution3:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        pointer1, pointer2, curr = m - 1, n - 1, n + m - 1

        for curr in range(n + m - 1, -1, -1):
            if pointer2 < 0 or pointer1 >= 0 and nums1[pointer1] > nums2[pointer2]:
                nums1[curr] = nums1[pointer1]
                pointer1 -= 1
            else:
                nums1[curr] = nums2[pointer2]
                pointer2 -= 1


def main():
    pass


if __name__ == '__main__':
    main()
