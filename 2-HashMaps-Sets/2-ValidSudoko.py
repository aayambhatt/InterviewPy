from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_sets = [set() for _ in range(9)]
        col_sets = [set() for _ in range(9)]
        subgrid_sets = [[set() for _ in range(3)] for _ in range(3)]

        for rows in range(9):
            for cols in range(9):
                num = board[rows][cols]
                if num =='.':
                    continue
                if num in row_sets[rows]:
                    return False
                if num in col_sets[cols]:
                    return False
                if num in subgrid_sets[rows//3][cols//3]:
                    return False
            
                row_sets[rows].add(num)
                col_sets[cols].add(num)
                subgrid_sets[rows//3][cols//3].add(num)
        
        return True

        