# https://leetcode.com/problems/simplify-path/

import re


class Solution:
    def simplify(self, path: str):
        simplified_path = []
        for name_dir in re.split(r'/+', path):
            if not name_dir or name_dir == '.':
                continue
            if name_dir == '..':
                if simplified_path:
                    simplified_path.pop()
            else:
                simplified_path.append(name_dir)
        return '/' + '/'.join(simplified_path)


def main():
    print(Solution().simplify('/home/lib/../path//.../'))


if __name__ == '__main__':
    main()
