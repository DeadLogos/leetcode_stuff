# https://leetcode.com/problems/rotate-image/


class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range((n + 1) // 2):
            for j in range(i, n - i - 1):
                matrix[j][-i - 1], temp = matrix[i][j], matrix[j][-i - 1]
                matrix[-i - 1][-j - 1], temp = temp, matrix[-i - 1][-j - 1]
                matrix[-j - 1][i], temp = temp, matrix[-j - 1][i]
                matrix[i][j] = temp


def main():
    arr = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    print(*arr, sep='\n')
    Solution().rotate(arr)
    print()
    print(*arr, sep='\n')


if __name__ == '__main__':
    main()
