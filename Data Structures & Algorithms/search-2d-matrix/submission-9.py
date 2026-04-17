class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # we care about the last val of each array 
        ROW, COL = len(matrix), len(matrix[0])
        left = 0
        right = (ROW*COL)-1
        while left <= right:
            mid = left + ((right-left)//2)
            row = mid // (COL)
            col = mid % (COL)
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

