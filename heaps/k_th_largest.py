# https://leetcode.com/problems/kth-largest-element-in-an-array/

import heapq
import random


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)
        for i in range(k, len(nums)):
            if nums[i] > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, nums[i])
        return heap[0]


class Solution2:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        min_bound, max_bound = min(nums), max(nums)
        counting_arr = [0] * (max_bound - min_bound + 1)
        for elem in nums:
            counting_arr[elem - min_bound] += 1

        for i in range(len(counting_arr) - 1, -1, -1):
            if k - counting_arr[i] <= 0:
                return i + min_bound
            k -= counting_arr[i]


class Solution3:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        def helper(arr, k):
            pivot = random.choice(arr)
            left, middle, right = [], [], []
            for elem in arr:
                if elem < pivot:
                    left.append(elem)
                elif elem == pivot:
                    middle.append(elem)
                else:
                    right.append(elem)

            if len(right) >= k:
                return helper(right, k)
            elif len(right) + len(middle) < k:
                return helper(left, k - len(right) - len(middle))
            return pivot

        return helper(nums, k)


def main():
    pass


if __name__ == '__main__':
    main()
