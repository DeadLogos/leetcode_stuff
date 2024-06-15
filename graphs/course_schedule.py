# https://leetcode.com/problems/course-schedule/description/

from collections import defaultdict as dd


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = {i: set() for i in range(numCourses)}
        for node, pre_node in prerequisites:
            graph[pre_node].add(node)

        used = set()

        def dfs(curr_node):
            if curr_node in used:
                return False
            if not graph[curr_node]:
                return True

            used.add(curr_node)
            for child in graph[curr_node]:
                if not dfs(child):
                    return False
            graph[curr_node].clear()
            used.discard(curr_node)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


class Solution2:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = dd(set)
        for parent, child in prerequisites:
            graph[parent].add(child)

        def dfs(i, used):
            if i in used:
                return False
            used.add(i)
            for node in graph[i]:
                if not dfs(node, used):
                    return False
            used.discard(i)
            graph[i].clear()
            return True

        for k in range(numCourses):
            if not dfs(k, set()):
                return False
        return True


def main():
    pass


if __name__ == '__main__':
    main()
