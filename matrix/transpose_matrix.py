# https://leetcode.com/problems/transpose-matrix/description/


class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        m, n = len(matrix), len(matrix[0])
        mat = []
        for j in range(n):
            row = []
            for i in range(m):
                row.append(matrix[i][j])
            mat.append(row)
        return mat


def main():
    pass


if __name__ == '__main__':
    main()
