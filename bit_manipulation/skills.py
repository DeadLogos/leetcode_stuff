# https://leetcode.com/problems/smallest-sufficient-team/description/


class Solution:
    def smallestSufficientTeam(self, req_skills: list[str], people: list[list[str]]) -> list[int]:
        skill_bits = {skill: 1 << i for i, skill in enumerate(req_skills)}
        dp = [None] * (2 ** len(req_skills))
        dp[0] = 0
        for i, person in enumerate(people):
            person_mask = sum(skill_bits[skill] for skill in person)
            for curr_skill_mask, set_mask in enumerate(dp):
                if set_mask is None:
                    continue
                new_skill_mask = curr_skill_mask | person_mask
                new_set_mask = set_mask | 1 << i
                if dp[new_skill_mask] is None or new_set_mask.bit_count() < dp[new_skill_mask].bit_count():
                    dp[new_skill_mask] = new_set_mask
        return [i for i, char in enumerate(bin(dp[-1])[:1:-1]) if char == '1']


def main():
    pass


if __name__ == '__main__':
    main()
