import math


def f_activate(X):
    for i in range(len(X)):
        X[i][0] = sigma(X[i][0])
    return X


def sigma(x):
    return 1 / (1 + math.exp(-x))


def sumMatrix(A, B):
    C = []
    for i in range(len(A)):
        lst = []
        for j in range(len(A[0])):
            lst.append(A[i][j] + B[i][j])
        C.append(lst)

    return C


def minus(A, B):
    C = []
    for i in range(len(A)):
        lst = []
        for j in range(len(A[0])):
            lst.append(A[i][j] - B[i][j])
        C.append(lst)

    return C


def minusConst(A, con):
    C = [[0]*len(A[0]) for i in range(len(A))]

    for i in range(len(A)):
        for j in range(len(A[0])):
            C[i][j] = con - A[i][j]

    return C


def multElement(A, B):
    m = len(A)
    n = len(A[0])
    C = [[0]*n for i in range(m)]

    for i in range(m):
        for j in range(n):
            C[i][j] = A[i][j] * B[i][j]

    return C


def mult(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    if (cols_A != rows_B):
        print('error')
        return

    C = [[0 for row in range(cols_B)] for col in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += A[i][k] * B[k][j]

    return C


def multConst(A, con):
    m = len(A)
    n = len(A[0])
    C = [[0]*n for i in range(m)]

    for i in range(m):
        for j in range(n):
            C[i][j] = A[i][j] * con

    return C


def transpose(A):
    C = [[0]*len(A) for i in range(len(A[0]))]

    for i in range(len(A[0])):
        for j in range(len(A)):
            C[i][j] = A[j][i]

    return C


if __name__ == '__main__:':
    A = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

    B = [[1],
         [2],
         [3]]

    m = len(A)
    n = len(A[0])

    print(f'размер матрицы - {m}X{n}')

    summ = 0
    avg = 0

    for i in range(m):
        for j in range(n):
            print(A[i][j], end=' ')
            summ += A[i][j]
        print()

    avg = summ / (m*n)
    print(summ)
    print(avg)

    print('-'*30)

    print(mult(A, B))
