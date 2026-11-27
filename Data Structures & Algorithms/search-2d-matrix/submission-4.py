
class Solution:
    def searchMatrix(self, matrix, target):
        low = 0
        high = len(matrix[0]) * len(matrix) - 1

        while low <= high:
            mid = (low + high) // 2

            row = mid // len(matrix[0])
            col = mid % len(matrix[0])

            if matrix[row][col] < target:
                low = mid + 1
            elif matrix[row][col] > target:
                high = mid - 1
            else:
                return True

        return False
