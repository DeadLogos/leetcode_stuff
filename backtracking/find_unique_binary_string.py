# https://leetcode.com/problems/find-unique-binary-string/


class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        strs = set(nums)

        def backtrack(i, curr: list) -> str:
            if i == len(curr):
                res = ''.join(curr)
                return res if res not in strs else ''
            res = backtrack(i + 1, curr)
            if res:
                return res
            curr[i] = '1'
            return backtrack(i + 1, curr)

        return backtrack(0, ['0'] * len(nums))


class Solution2:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        strs = set(nums)
        for x in range(len(nums) + 1):
            bin_x = f'{x:0>{len(nums)}b}'
            if bin_x not in strs:
                return bin_x


def main():
    pass


if __name__ == '__main__':
    main()
