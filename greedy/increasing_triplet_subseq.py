# https://leetcode.com/problems/increasing-triplet-subsequence/


class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        curr_min, greater_than_curr_min = nums[0], float('inf')
        for x in nums:
            if x > greater_than_curr_min:
                return True
            elif x > curr_min:
                greater_than_curr_min = x
            else:
                curr_min = x
        return False


def main():
    pass


if __name__ == '__main__':
    main()
