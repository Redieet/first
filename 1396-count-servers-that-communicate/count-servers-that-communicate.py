from typing import List

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        # Get the dimensions of the grid
        m, n = len(grid), len(grid[0])

        # Count the number of servers in each row and column
        row_count = [0] * m
        col_count = [0] * n

        # Populate the row and column counts
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1

        # Count the servers that can communicate
        communicating_servers = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    # A server can communicate if there's another server in the same row or column
                    if row_count[i] > 1 or col_count[j] > 1:
                        communicating_servers += 1

        return communicating_servers

        