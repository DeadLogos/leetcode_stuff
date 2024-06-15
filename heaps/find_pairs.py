# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/

import heapq


class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        heap, used = [(nums1[0] + nums2[0], 0, 0)], {(0, 0)}
        res = []
        for _ in range(min(k, len(nums1) * len(nums2))):
            _, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            if i + 1 < len(nums1) and (i + 1, j) not in used:
                heapq.heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
                used.add((i + 1, j))
            if j + 1 < len(nums2) and (i, j + 1) not in used:
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
                used.add((i, j + 1))
        return res


def main():
    pass


if __name__ == '__main__':
    main()
