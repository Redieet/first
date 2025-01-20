from typing import List

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        position = {}
        for i in range(m):
            for j in range(n):
                position[mat[i][j]] = (i, j)
        row_paint_count = [0] * m
        col_paint_count = [0] * n
        for idx, num in enumerate(arr):
            x, y = position[num]  
            row_paint_count[x] += 1
            col_paint_count[y] += 1
            if row_paint_count[x] == n or col_paint_count[y] == m:
                return idx

        return -1 
