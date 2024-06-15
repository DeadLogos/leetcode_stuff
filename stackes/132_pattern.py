# https://leetcode.com/problems/132-pattern/


class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        stack = [nums[0]]
        min_stack = [nums[0]]
        for i in range(1, len(nums)):
            x, last_min = nums[i], min(nums[i], min_stack[-1])
            while stack and stack[-1] < x:
                stack.pop()
                min_stack.pop()

            if stack and min_stack[-1] < x < stack[-1]:
                return True
            stack.append(x)
            min_stack.append(last_min)
        return False


class Solution2:
    def find132pattern(self, nums: list[int]) -> bool:
        stack = [0]
        min_values = [nums[0]]
        for i in range(1, len(nums)):
            min_values.append(min(min_values[-1], nums[i]))
        for i in range(1, len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()
            if stack and min_values[stack[-1]] < nums[i] < nums[stack[-1]]:
                return True
            stack.append(i)
        return False


class Solution3:
    def find132pattern(self, nums: list[int]) -> bool:
        stack = [(nums[0], nums[0])]
        curr_min = nums[0]
        for i in range(1, len(nums)):
            x = nums[i]
            while stack and x > stack[-1][0]:
                stack.pop()
            if stack and stack[-1][1] < x < stack[-1][0]:
                return True
            stack.append((x, curr_min))
            curr_min = min(curr_min, x)
        return False


def main():
    pass


if __name__ == '__main__':
    main()
