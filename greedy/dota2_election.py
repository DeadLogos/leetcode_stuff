# https://leetcode.com/problems/dota2-senate/

from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rest_voters = {'D': senate.count('D'), 'R': senate.count('R')}
        need_to_ban = {'D': 0, 'R': 0}
        que = deque(senate)
        while rest_voters['D'] and rest_voters['R']:
            senator = que.popleft()
            if need_to_ban[senator]:
                need_to_ban[senator] -= 1
                rest_voters[senator] -= 1
            else:
                need_to_ban['D' if senator == 'R' else 'R'] += 1
                que.append(senator)
        return 'Dire' if rest_voters['D'] else 'Radiant'


def main():
    pass


if __name__ == '__main__':
    main()
