from copy import deepcopy
import numpy as np

class MatrixError(BaseException):
    def __init__(self, matrix1, matrix2):
        self.matrix = matrix1
        self.matrix2 = matrix2


class Matrix:
    def __init__(self, matrix):
        self.matrix = deepcopy(matrix)

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, list)) for list in self.matrix])

    def size1(self):
        stroki = len(self.matrix)
        stolbi = 0
        for strok in self.matrix:
            if len(strok) > stolbi:
                stolbi = len(strok)
        return (stroki, stolbi)

    def __add__(self, matrix2):
        if self.size1(self) == self.size1(other):
            result = []
            for i in range(len(self.matrix)):
                res = []
                for j in range(len(self.matrix[0])):
                    res.append(self.matrix[i][j] + matrix2.matrix[i][j])
                result.append(res)
            return Matrix(result)
        else:
            error = MatrixError(self, other)
            raise error

    def helpmul(self):
        s = []
        for i in range(len(self.matrix)):
            s.append(self.matrix[i])
        return s

    def __mul__(self, other):
        if isinstance(other, Matrix):
            if len(self.matrix[0]) == other.size()[0]:
                a = np.array(self.matrix)
                b = np.array(other.helpmul())
                res = a.dot(b)
                result = []
                for i in range(len(res)):
                    result.append(res[i])
            else:
                error = MatrixError(self, other)
                raise error
        else:
            result = []
            for i in range(len(self.matrix)):
                res = []
                for j in range(len(self.matrix[0])):
                    res.append(self.matrix[i][j] * other)
                result.append(res)
        return Matrix(result)

    __rmul__ = __mul__

    def transpose(self):
        x = []
        for i in range(len(self.matrix)):
            x.append(i)
            for j in range(len(self.matrix[0])):
                if j not in x:
                    self.matrix[i][j], self.matrix[j][i] = self.matrix[j][i], self.matrix[i][j]
        return Matrix(self.matrix)

    @staticmethod
    def transposed(self):
        x = []
        for i in range(len(self.matrix)):
            x.append(i)
            for j in range(len(self.matrix[0])):
                if j not in x:
                    self.matrix[i][j], self.matrix[j][i] = self.matrix[j][i], self.matrix[i][j]
        return Matrix(self.matrix)

    def solve(self, vector):
        a = np.array(self.matrix)
        b = np.array(vector)
        res = np.linalg.solve(a, b)
        result = []
        for i in range(len(res)):
            result.append(res[i])
        if not isinstance(result, list):
            error = MatrixError(self, vector)
            raise error
        return result





mid = Matrix([[1,1,1],[0,2,0],[0,0,4]])
print(mid.solve([1,1,1]))
