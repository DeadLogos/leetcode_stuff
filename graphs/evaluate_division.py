# https://leetcode.com/problems/evaluate-division/

from collections import defaultdict


class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        graph = defaultdict(dict)
        for i, (var1, var2) in enumerate(equations):
            graph[var1][var2] = values[i]
            graph[var2][var1] = 1 / values[i]

        def dfs(curr_var, finish_var, value, used):
            used.add(curr_var)
            if curr_var == finish_var:
                res.append(value)
                return True
            for next_var, next_value in graph[curr_var].items():
                if next_var not in used and dfs(next_var, finish_var, value * next_value, used):
                    return True
            return False

        res = []
        for var1, var2 in queries:
            if var1 not in graph or var2 not in graph or not dfs(var1, var2, 1, set()):
                res.append(-1.0)
        return res


class Solution2:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        graph = defaultdict(dict)
        for i, (var1, var2) in enumerate(equations):
            graph[var1][var2] = values[i]
            graph[var2][var1] = 1 / values[i]

        def dfs(curr_var, finish_var, value, used):
            used.add(curr_var)
            if curr_var == finish_var:
                return value if finish_var in graph else -1.0
            for next_var, next_value in graph.get(curr_var, {}).items():
                if next_var not in used:
                    res = dfs(next_var, finish_var, value * next_value, used)
                    if res != -1.0:
                        return res
            return -1.0

        return [dfs(var1, var2, 1, set()) for var1, var2 in queries]


def main():
    pass


if __name__ == '__main__':
    main()
