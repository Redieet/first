from collections import deque
from typing import List

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(grid), len(grid[0])
        cost = [[float('inf')] * n for _ in range(m)]
        dq = deque([(0, 0, 0)])  # (row, col, current_cost)
        cost[0][0] = 0

        while dq:
            x, y, c = dq.popleft()
            if c > cost[x][y]:
                continue

            for i, (dx, dy) in enumerate(directions):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    new_cost = c + (1 if grid[x][y] != i + 1 else 0)
                    if new_cost < cost[nx][ny]:
                        cost[nx][ny] = new_cost
                        if grid[x][y] == i + 1:
                            dq.appendleft((nx, ny, new_cost))
                        else:
                            dq.append((nx, ny, new_cost))

        return cost[m - 1][n - 1]

        