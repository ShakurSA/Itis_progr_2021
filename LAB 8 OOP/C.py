from sys import stdin
from copy import deepcopy


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

    def __mul__(self, number):
        result = []
        if isinstance(int, number) or isinstance(float, number):
            for i in range(len(self.matrix)):
                res = []
                for j in range(len(self.matrix[0])):
                    res.append(self.matrix[i][j] * number)
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


mat = ([[1,2], [3,4],[5,6]])
inst = Matrix(mat)
print(inst)
print(' ')
print(inst.transpose())
exec(stdin.read())

