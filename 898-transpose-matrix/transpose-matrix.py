class Solution:
    def transpose(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        # Create empty transpose matrix
        answer = [[0] * rows for _ in range(cols)]

        # Fill transpose
        for i in range(rows):
            for j in range(cols):
                answer[j][i] = matrix[i][j]

        return answer