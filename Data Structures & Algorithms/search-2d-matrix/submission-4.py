class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        row_num = 0
        for row in range(len(matrix)):
            if matrix[row][0] >= target:
                if matrix[row][0] == target:
                    return True
                else:
                    row_num = row - 1
                    break
            row_num = row

        return target in matrix[row_num]
        