class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # to make this efficient, we should break this 2d array into a 
        # 1d array and then do binary search
        ROWS, COLS = len(matrix), len(matrix[0])
        left = 0
        right = (ROWS*COLS)-1
        while left <= right:
            mid = left + ((right-left)//2)
            row = mid//COLS
            col = mid%COLS
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
    

