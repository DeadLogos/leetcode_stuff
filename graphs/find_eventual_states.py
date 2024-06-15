# https://leetcode.com/problems/find-eventual-safe-states/description/


class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        is_safe = [False] * len(graph)
        used = [False] * len(graph)

        def dfs(node, curr_used):
            if used[node]:
                return is_safe[node]
            if is_safe[node]:
                return True

            used[node] = True
            curr_used.add(node)
            for child in graph[node]:
                if child in curr_used or not dfs(child, curr_used):
                    curr_used.discard(node)
                    return False
            curr_used.discard(node)
            is_safe[node] = True
            return True

        for i in range(len(graph)):
            dfs(i, set())

        return [i for i in range(len(graph)) if is_safe[i]]


class Solution2:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        is_safe = {}

        def dfs(node):
            if node in is_safe:
                return is_safe[node]

            is_safe[node] = False
            for child in graph[node]:
                if not dfs(child):
                    return False
            is_safe[node] = True
            return True

        res = []
        for i in range(len(graph)):
            if dfs(i):
                res.append(i)
        return res


def main():
    pass


if __name__ == '__main__':
    main()
