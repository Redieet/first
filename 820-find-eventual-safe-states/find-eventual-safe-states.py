from typing import List
from collections import deque

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        reverse_graph = [[] for _ in range(n)]
        indegree = [0] * n

        for u in range(n):
            for v in graph[u]:
                reverse_graph[v].append(u)
                indegree[u] += 1

        queue = deque([i for i in range(n) if indegree[i] == 0])
        safe_nodes = []

        while queue:
            node = queue.popleft()
            safe_nodes.append(node)
            for neighbor in reverse_graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return sorted(safe_nodes)
