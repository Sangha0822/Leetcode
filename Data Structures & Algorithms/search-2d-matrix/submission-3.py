class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        find = -1
        for i in range(len(matrix)):
            if matrix[i][-1] >= target:
                if matrix[i][-1] == target:
                    return True
                find = i
                break
        if find != -1:
            for i in range(len(matrix[find])):
                if matrix[find][i] == target:
                    return True
        return False