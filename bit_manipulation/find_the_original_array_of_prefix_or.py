# https://leetcode.com/problems/find-the-original-array-of-prefix-xor/


class Solution:
    def findArray(self, pref: list[int]) -> list[int]:
        arr = [pref[0]]
        for i in range(1, len(pref)):
            arr.append(pref[i - 1] ^ pref[i])
        return arr


def main():
    pass


if __name__ == '__main__':
    main()
