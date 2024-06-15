# https://leetcode.com/problems/minimum-cost-to-make-array-equal/description/


class Solution:
    def minCost(self, nums: list[int], cost: list[int]) -> int:
        res = float('inf')
        for i in range(len(nums)):
            curr_cost = 0
            for j in range(len(nums)):
                if i != j:
                    curr_cost += cost[j] * abs(nums[i] - nums[j])
            res = min(curr_cost, res)
        return res


class Solution2:
    def minCost(self, nums: list[int], cost: list[int]) -> int:
        sorted_nums = sorted(zip(nums, cost))

        curr_cost = sum(price * (point - sorted_nums[0][0]) for point, price in sorted_nums)
        step_price = -sum(map(lambda x: x[1], sorted_nums)) + sorted_nums[0][1] * 2
        prev_point = sorted_nums[0][0]

        for i in range(1, len(nums)):
            if step_price >= 0:
                return curr_cost
            point, price = sorted_nums[i]
            curr_cost += step_price * (point - prev_point)
            step_price += price * 2
            prev_point = point

        return curr_cost


class Solution3:
    def minCost(self, nums: list[int], cost: list[int]) -> int:
        sorted_nums = sorted(zip(nums, cost))
        step_price = -sum(map(lambda x: x[1], sorted_nums))  # change of total cost per step

        # when step_price becomes non-negative -> we reach the goal(minimum total cost to equalize)
        for i in range(len(nums)):
            point, price = sorted_nums[i]
            step_price += price * 2
            if step_price >= 0:
                return sum(price * abs(x - point) for x, price in sorted_nums)


def main():
    pass


if __name__ == '__main__':
    main()
