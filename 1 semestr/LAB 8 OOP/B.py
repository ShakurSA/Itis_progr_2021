from sys import stdin
from copy import deepcopy


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
        result = []
        for i in range(len(self.matrix)):
            res = []
            for j in range(len(self.matrix[0])):
                res.append(self.matrix[i][j] + matrix2.matrix[i][j])
            result.append(res)
        return Matrix(result)

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

mid = Matrix([[1,0,0],[0,1,0],[0,0,1]])
m1 = Matrix([[3, 2, 4], [-10, 0, 6], [14,5, 20]])
print(mid+m1)
exec(stdin.read())
