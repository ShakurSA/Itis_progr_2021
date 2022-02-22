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

matrix = ([[1,2], [3,4],[5,6]])
inst = Matrix(matrix)
print(inst)
print(inst.size1())
exec(stdin.read())