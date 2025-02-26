import random

class MatrixOperations:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0]) if matrix else 0

    def multiply(self, other):
        if self.cols != len(other.matrix):
            raise ValueError("Cannot multiply: Column count of first matrix must match row count of second matrix")
        
        result = [[0 for _ in range(len(other.matrix[0]))] for _ in range(self.rows)]
        
        for i in range(self.rows):
            for j in range(len(other.matrix[0])):
                for k in range(self.cols):
                    result[i][j] += self.matrix[i][k] * other.matrix[k][j]
        
        return MatrixOperations(result)

    def transpose(self):
        result = [[self.matrix[j][i] for j in range(self.rows)] for i in range(self.cols)]
        return MatrixOperations(result)

    def determinant(self):
        if self.rows != self.cols:
            raise ValueError("Determinant is only defined for square matrices")
        return self._calculate_determinant(self.matrix)

    def _calculate_determinant(self, matrix):
        if len(matrix) == 1:
            return matrix[0][0]
        if len(matrix) == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

        det = 0
        for c in range(len(matrix)):
            minor = [row[:c] + row[c+1:] for row in matrix[1:]]
            det += ((-1) ** c) * matrix[0][c] * self._calculate_determinant(minor)
        return det

    def display(self):
        for row in self.matrix:
            print(row)
        print()

# Example usage
matrix_a = MatrixOperations([[random.randint(1, 5) for _ in range(3)] for _ in range(3)])
matrix_b = MatrixOperations([[random.randint(1, 5) for _ in range(3)] for _ in range(3)])

print("Matrix A:")
matrix_a.display()

print("Matrix B:")
matrix_b.display()

print("A * B:")
result = matrix_a.multiply(matrix_b)
result.display()

print("Transpose of A:")
matrix_a.transpose().display()

print("Determinant of A:", matrix_a.determinant())


import numpy as np

class MatrixOperations:
    def __init__(self, matrix):
        self.matrix = np.array(matrix)

    def multiply(self, other):
        return MatrixOperations(np.dot(self.matrix, other.matrix))

    def transpose(self):
        return MatrixOperations(self.matrix.T)

    def determinant(self):
        if self.matrix.shape[0] != self.matrix.shape[1]:
            raise ValueError("Determinant is only defined for square matrices")
        return np.linalg.det(self.matrix)

    def display(self):
        print(self.matrix, "\n")

# Example usage
matrix_a = MatrixOperations(np.random.randint(1, 6, (3, 3)))
matrix_b = MatrixOperations(np.random.randint(1, 6, (3, 3)))

print("Matrix A:")
matrix_a.display()

print("Matrix B:")
matrix_b.display()

print("A * B:")
result = matrix_a.multiply(matrix_b)
result.display()

print("Transpose of A:")
matrix_a.transpose().display()

print("Determinant of A:", matrix_a.determinant())
