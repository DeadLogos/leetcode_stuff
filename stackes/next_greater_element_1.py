# https://leetcode.com/problems/next-greater-element-i/


class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        next_greater_elements = {}
        stack = []
        for x in nums2:
            while stack and stack[-1] < x:
                next_greater_elements[stack.pop()] = x
            stack.append(x)
        next_greater_elements.update(dict.fromkeys(stack, -1))
        return [next_greater_elements[x] for x in nums1]


class Solution2:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        next_greater_elements = {}
        stack = []
        for i in range(len(nums2) - 1, -1, -1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            next_greater_elements[nums2[i]] = stack[-1] if stack else -1
            stack.append(nums2[i])
        return [next_greater_elements[x] for x in nums1]


def main():
    pass


if __name__ == '__main__':
    main()
