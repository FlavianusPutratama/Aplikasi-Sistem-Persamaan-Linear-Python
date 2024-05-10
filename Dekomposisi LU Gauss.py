import numpy as np

def lu_decomposition(A):
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for i in range(n):
        L[i][i] = 1

    for k in range(n):
        U[k][k] = A[k][k]

        for j in range(k+1, n):
            L[j][k] = A[j][k] / U[k][k]
            U[k][j] = A[k][j]

        for i in range(k+1, n):
            for j in range(k+1, n):
                A[i][j] = A[i][j] - L[i][k] * U[k][j]

    return L, U

def solve_lu_gauss(A, b):
    L, U = lu_decomposition(A)

    # Ly = b
    n = len(b)
    y = np.zeros(n)
    for i in range(n):
        y[i] = b[i]
        for j in range(i):
            y[i] -= L[i][j] * y[j]

    # Ux = y
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = y[i]
        for j in range(i+1, n):
            x[i] -= U[i][j] * x[j]
        x[i] /= U[i][i]

    return x

# Contoh penggunaan:
A = np.array([[2, -1, 1], [-3, -1, 2], [-2, 1, 2]])
b = np.array([8, -11, -3])

solusi = solve_lu_gauss(A, b)
print("Solusi sistem persamaan linear:")
print(solusi)
