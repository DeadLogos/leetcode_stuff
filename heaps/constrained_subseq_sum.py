# https://leetcode.com/problems/constrained-subsequence-sum/

import heapq


class Solution:
    def constrainedSubsetSum(self, nums: list[int], k: int) -> int:
        heap = []
        dp = [0] * len(nums)
        for i in range(len(nums)):
            while heap and heap[0][1] < i - k:
                heapq.heappop(heap)
            dp[i] = (-heap[0][0] if heap else 0) + nums[i]
            if dp[i] > 0:
                heapq.heappush(heap, (-dp[i], i))
        return max(dp)


def main():
    pass


if __name__ == '__main__':
    main()
