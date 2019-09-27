class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # Clockwise Direction: Transpose, then take reverse of each colunn
        # CCW Direction: Reverse of each column, then transpose
        
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for c in matrix:
            c.reverse()

        return matrix
