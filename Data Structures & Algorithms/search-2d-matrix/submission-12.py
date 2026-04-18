class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        matrix_rows, matrix_cols = len(matrix), len(matrix[0])
        left = 0
        right = (matrix_rows*matrix_cols)-1
        while left <= right:
            mid = left + ((right-left)//2)
            row = mid//matrix_cols
            col = mid%matrix_cols
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False