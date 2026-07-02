class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr = [item for row in matrix for item in row]

        return target in arr