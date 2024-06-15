# https://leetcode.com/problems/buddy-strings/


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        indexes = []
        for i, char in enumerate(s):
            if char != goal[i]:
                indexes.append(i)
            if len(indexes) > 2:
                return False

        return len(indexes) == 2 and s[indexes[0]] == goal[indexes[1]] and \
            s[indexes[1]] == goal[indexes[0]] or not indexes and len(set(s)) < len(s)


def main():
    pass


if __name__ == '__main__':
    main()
