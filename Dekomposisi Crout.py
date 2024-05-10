import numpy as np

def crout_decomposition(A):
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for i in range(n):
        # Mendekomposisi U
        for k in range(i, n):
            sum = 0
            for j in range(i):
                sum += (L[i][j] * U[j][k])
            U[i][k] = A[i][k] - sum

        # Mendekomposisi L
        for k in range(i, n):
            if (i == k):
                L[i][i] = 1  # Diagonal 1
            else:
                sum = 0
                for j in range(i):
                    sum += (L[k][j] * U[j][i])
                L[k][i] = (A[k][i] - sum) / U[i][i]

    return L, U

def solve_linear_equation(A, b):
    L, U = crout_decomposition(A)
    n = len(A)
    y = np.zeros(n)
    x = np.zeros(n)

    # Memecahkan Ly = b
    for i in range(n):
        sum = 0
        for j in range(i):
            sum += L[i][j] * y[j]
        y[i] = (b[i] - sum) / L[i][i]

    # Memecahkan Ux = y
    for i in range(n - 1, -1, -1):
        sum = 0
        for j in range(i + 1, n):
            sum += U[i][j] * x[j]
        x[i] = (y[i] - sum) / U[i][i]

    return x

# Contoh penggunaan
A = np.array([[2, -1, 1],
              [-3, -1, 4],
              [-1, 1, 3]])
b = np.array([2, 1, -3])

x = solve_linear_equation(A, b)
print("Solusi sistem persamaan linear:")
print(x)
