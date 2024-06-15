# https://leetcode.com/problems/subsets/description/


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        self.subset = []
        self.res = []
        self.total = 0

        def backtrack(i):
            self.total += 1
            if i == len(nums):
                self.res.append(self.subset.copy())
                return

            backtrack(i + 1)

            self.subset.append(nums[i])
            backtrack(i + 1)
            self.subset.pop()

        backtrack(0)
        print(self.total)
        return self.res


class Solution2:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        self.subset = []
        self.res = []
        self.total = 0

        def backtrack(i):
            self.total += 1
            self.res.append(self.subset.copy())

            for j in range(i, len(nums)):
                self.subset.append(nums[j])
                backtrack(j + 1)
                self.subset.pop()

        backtrack(0)
        print(self.total)
        return self.res


def main():
    pass


if __name__ == '__main__':
    main()
