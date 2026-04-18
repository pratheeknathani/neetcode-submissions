class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            low, high = 0, len(matrix[0])-1
            low_row = matrix[i][low]
            high_row = matrix[i][high]
            while low<= high:
                iterator = low + ((high-low)//2)
                if matrix[i][iterator] == target:
                    return True
                elif high_row<target:
                    break
                elif target>low_row:
                    low = iterator +1
                else:
                    high = iterator -1
        return False
