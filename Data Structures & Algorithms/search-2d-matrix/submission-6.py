class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # we care about the last val of each array 
        # if 
        for i in matrix:
            print(i[-1])
            if i[-1] < target:
                continue
            left = 0
            right = len(i)-1
            while left <= right:
                mid = left + ((right-left)//2)
                print(mid)
                if i[mid] == target:
                    return True
                elif i[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
        return False