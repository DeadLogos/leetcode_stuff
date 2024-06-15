# https://leetcode.com/problems/find-smallest-letter-greater-than-target/


class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        left, right = -1, len(letters)
        while left + 1 < right:
            middle = (left + right) // 2
            if letters[middle] <= target:
                left = middle
            else:
                right = middle
        return letters[0] if right == len(letters) else letters[right]


def main():
    arr = ['x', 'x', 'y', 'y']
    print(Solution().nextGreatestLetter(arr, 'z'))


if __name__ == '__main__':
    main()
