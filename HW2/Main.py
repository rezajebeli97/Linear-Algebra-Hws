import numpy as np
from scipy.linalg import hilbert


def lu(A):
    n = A.shape[0]
    n1 = A.shape[0]
    if n != n1:
        print("You should insert a square matrix!")

    L = np.eye(n)
    U = np.zeros((n, n))

    for j in range(0, n):

        for i in range(0, j + 1):
            s1 = sum(U[k][j] * L[i][k] for k in range(i))
            U[i][j] = A[i][j] - s1
            for i in range(j, n):
                s2 = sum(U[k][j] * L[i][k] for k in range(j))
                L[i][j] = (A[i][j] - s2) / U[j][j]
    return (L, U)


def forward(A):
    A = np.array(A)
    n = A.shape[0]
    for i in range(0, n):
        for k in range(i + 1, n):
            c = -A[k][i] / A[i][i]
            for j in range(i, n + 1):
                if i == j:
                    A[k][j] = 0
                else:
                    A[k][j] += c * A[i][j]
    return A[:, A.shape[1] - 1]


def backward(A):
    A = np.array(A)
    n = A.shape[0]

    for i in range(n - 1, -1, -1):

        A[i][n] = A[i][n] / A[i][i]
        A[i][n] = np.round(A[i][n], 6)
        A[i][i] = 1
        for k in range(i - 1, -1, -1):
            A[k][n] -= A[k][i] * A[i][n]
            A[k][i] = 0

    for i in range(0, n):
        A[i][n] = np.round(A[i][n], 6)

    return A[:, n]


def linear_sys_solver(A, b):
    L, U = lu(A)
    Lb = np.zeros((L.shape[0], L.shape[1] + 1))
    Lb[:, 0:L.shape[1]] = L
    Lb[:, L.shape[1]] = b
    y = forward(Lb)
    Uy = np.zeros((U.shape[0], U.shape[1] + 1))
    Uy[:, 0:U.shape[1]] = U
    Uy[:, U.shape[1]] = y
    x = backward(Uy)
    return x


def myInverse(A):
    I = np.eye(A.shape[0])
    n = A.shape[0]
    Ainv = np.zeros(A.shape)
    L, U = lu(A)
    for i in range(0, n):
        b = I[:, i]
        Lb = np.zeros((L.shape[0], L.shape[1] + 1))
        Lb[:, 0:L.shape[1]] = L
        Lb[:, L.shape[1]] = b
        y = forward(Lb)
        Uy = np.zeros((U.shape[0], U.shape[1] + 1))
        Uy[:, 0:U.shape[1]] = U
        Uy[:, U.shape[1]] = y
        x = backward(Uy)
        Ainv[:, i] = x
    return Ainv


def partD():
    for x in range(2, 3):
        H = hilbert(x * 5)
        Ainv = np.linalg.inv(H)
        A_prim_Inv = myInverse(H)
        A_Ainv = np.matmul(H, Ainv)
        A_A_Prim_Inv = np.matmul(H, A_prim_Inv)

        print("n = ", x * 5)
        print("inverse = ")
        print(A_prim_Inv)
        print("A'inv * A =")
        print(A_A_Prim_Inv)

        print("result = ")
        print(Ainv)
        print("Ainv * A :")
        print(A_Ainv)

A = [[1,2],[3,4]]

Ap = myInverse(np.array(A))

print(Ap)