# https://leetcode.com/problems/product-of-array-except-self/description/


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [1] * n
        curr_product = curr_product_reverse = 1
        for i in range(n):
            ans[i] *= curr_product
            curr_product *= nums[i]
            ans[n - i - 1] *= curr_product_reverse
            curr_product_reverse *= nums[n - i - 1]
        return ans


def main():
    pass


if __name__ == '__main__':
    main()
